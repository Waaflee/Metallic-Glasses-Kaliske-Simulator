import json
from typing import Dict, List, TypedDict
import numpy as np
# Branch = TypedDict[{"E": float, "tau": float}]
# Data = TypedDict[{"E": float, "branches": List[Branch]}]


class Maxwell():

    def __init__(self, time: str, deformation: str):
        """Accepts the next simulation parameters:
            - time: str -> String in Octave notation '0:0.1:1'
            - time: str -> String in Octave notation '0:1'
                where the first item its the simulation start time,
                the second the simulation time step,
                and the third the simulation end time.
            - deformation: str -> String in Octave notation '0:0.1:1'
                where the first item its the simulation starting deformation,
                the second the simulation deformation step,
                and the third the simulation ending deformation.
        """
        # self.time_start, self.time_step, self.time_end = map(
        #     lambda x: float(x), time.split(":"))
        self.time_start, self.time_end = map(
            lambda x: float(x), time.split(":"))
        self.deformation_start, self.deformation_step, self.deformation_end = map(
            lambda x: float(x), deformation.split(":"))
        # read config file
        with open('models/maxwell/config.json', 'r') as config:
            self.data = json.loads(config.read())
            # print(self.data)
            # print(self.data["E"])
            # for i in self.data["branches"]:
            #     print(i)
            #     print(i["E"])
            #     print(i["tau"])

    def run(self):
        mu0: float = self.data["E"]
        deformation = np.arange(self.deformation_start,
                                self.deformation_end + self.deformation_step, self.deformation_step, dtype=np.float32)
        dt = (self.time_end - self.time_start) / (deformation.size - 1)
        time = np.arange(self.time_start, self.time_end + dt, dt)
        gamma = np.array([x["E"]/mu0 for x in self.data["branches"]])
        tau = np.array([x["tau"] for x in self.data["branches"]])

        h = np.empty((deformation.size, len(self.data["branches"])),
                     dtype=float, order='C')
        sigma = np.empty((deformation.size))
        sigma0 = np.array(list(map(lambda x: mu0*x, deformation)))
        for i in range(1, deformation.size):

            for j in range(0, len(self.data["branches"])):
                h[i, j] = np.e**(-dt / tau[j]) * h[i-1, j] + \
                    gamma[j] * (
                        ((1 - np.e**(-dt/tau[j])) / (dt / tau[j]))
                )*(sigma0[i]-sigma0[i-1])
            sigma[i] = mu0 * deformation[i] + h[i, :].sum()

        return (sigma, deformation, time)
