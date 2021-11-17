import json
from typing import Dict, List, NamedTuple, Tuple, TypedDict
import numpy as np


class Maxwell():

    def __init__(self, time: str, deformation: str, model: int = 0):
        """Accepts the next simulation parameters:
            - time: str -> String in Octave notation '0:0.1:1'
                where the first item its the simulation start time,
                the second the simulation time step,
                and the third the simulation end time.
            - deformation: str -> String in Octave notation '0:1'
                where the first item its the simulation starting deformation,
                and the second the simulation ending deformation.
        """
        self.time_start, self.time_step, self.time_end = map(
            lambda x: float(x), time.split(":"))

        self.deformation_start, self.deformation_end = map(
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
        dt = self.time_step

        time_length = int((self.time_end + dt - self.time_start) / dt)

        time: np.ndarray = np.linspace(
            self.time_start, self.time_end + dt, time_length + 1)

        deformation: np.ndarray = np.linspace(
            self.deformation_start, self.deformation_end, time.size)

        gamma: np.ndarray = np.array(
            [x["E"]/mu0 for x in self.data["branches"]])

        tau: np.ndarray = np.array([x["tau"] for x in self.data["branches"]])

        h: np.ndarray = np.zeros((deformation.size, len(self.data["branches"])),
                                 dtype=float, order='C')
        h += 0.1

        sigma: np.ndarray = np.empty((deformation.size))
        deformation[0] = 0
        sigma0: np.ndarray = np.array(list(map(lambda x: mu0*x, deformation)))
        sigma[0:] = sigma0[0:]

        for i in range(1, time.size):

            for j in range(0, len(self.data["branches"])):

                h[i, j] = np.e**(-dt / tau[j]) * h[i-1, j] + \
                    gamma[j] * (
                        ((1 - np.e**(-dt/tau[j])) / (dt / tau[j]))
                )*(sigma0[i]-sigma0[i-1])

            sigma[i] = mu0 * deformation[i] + h[i, :].sum()

        # return (sigma, deformation, time)
        return (sigma[1:], deformation[1:], time[1:] - dt)
