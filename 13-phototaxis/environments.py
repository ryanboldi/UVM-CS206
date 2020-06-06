import constants as c
from environment import ENVIRONMENT


class ENVIRONMENTS:
    def __init__(self):
        self.envs = {}
        for e in range(0, c.numEnvs):
            self.envs[e] = ENVIRONMENT(e)