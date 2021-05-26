import json


class Maxwell():

    def __init__(self, time: str, deformation: str):
        """Accepts the next simulation parameters:
            - time: str -> String in Octave notation '0:0.1:1'
                where the first item its the simulation start time,
                the second the simulation time step,
                and the third the simulation end time.
            - deformation: str -> String in Octave notation '0:0.1:1'
                where the first item its the simulation starting deformation,
                the second the simulation deformation step,
                and the third the simulation ending deformation.
        """
        self.time_start, self.time_step, self.time_end = map(
            lambda x: float(x), time.split(":"))
        self.deformation_start, self.deformation_step, self.deformation_end = map(
            lambda x: float(x), deformation.split(":"))
        # read config file
        with open('models/maxwell/config.json', 'r') as config:
            self.data = json.loads(config.read())
