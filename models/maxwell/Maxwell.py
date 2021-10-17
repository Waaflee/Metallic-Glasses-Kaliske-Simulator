import json
from typing import Dict, List, NamedTuple, Tuple, TypedDict
import numpy as np


class Maxwell():

    def __init__(self, time: str, deformation: str, model: int = 0):
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

        if (self.deformation_start > self.deformation_end):
            raise ValueError(
                "Initial deformation can't less than final deformation.")
        if (self.time_start > self.time_end):
            raise ValueError(
                "Initial time can't less than time time.")
        # read config file
        with open('models/maxwell/config.json', 'r') as config:
            self.data = json.loads(config.read())[int(model)]

    def run(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        mu0: float = self.data["E"]

        deformation: np.ndarray = np.arange(self.deformation_start,
                                            self.deformation_end + self.deformation_step, self.deformation_step, dtype=np.float32)

        dt = (self.time_end - self.time_start) / (deformation.size - 1)

        time: np.ndarray = np.arange(self.time_start, self.time_end + dt, dt)
        gamma: np.ndarray = np.array(
            [x["E"]/mu0 for x in self.data["branches"]])
        tau: np.ndarray = np.array([x["tau"] for x in self.data["branches"]])
        h: np.ndarray = np.empty((deformation.size, len(self.data["branches"])),
                                 dtype=float, order='C')

        sigma: np.ndarray = np.empty((deformation.size))
        sigma0: np.ndarray = np.array(list(map(lambda x: mu0*x, deformation)))

        for i in range(1, deformation.size):

            for j in range(0, len(self.data["branches"])):
                h[i, j] = np.e**(-dt / tau[j]) * h[i-1, j] + \
                    gamma[j] * (
                        ((1 - np.e**(-dt/tau[j])) / (dt / tau[j]))
                )*(sigma0[i]-sigma0[i-1])
            sigma[i] = mu0 * deformation[i] + h[i, :].sum()

        return (sigma, deformation, time)
