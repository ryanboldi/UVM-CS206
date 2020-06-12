import random
import pyrosim
import math
import numpy as np
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = np.random.rand(14,6) *2 -1
        self.fitness = 0
    
    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator( play_paused=True, eval_time=500, play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()

        #gets x,y,z coord of individual's red cylinder.
        y = self.sim.get_sensor_data(sensor_id=self.robot.P4 , svi = 1)

        self.fitness = y[-1] #gets last element in y array (last y pos)
        del self.sim

    def Mutate(self):
        rowToMutate = random.randint(0,len(self.genome) - 1)
        colToMutate = random.randint(0, len(self.genome[0]) -1)
        #new random value close to parent's random value
        #Standard deviation is |self.genome| to make the mutate take 
        # larger steps the larger the genome is
        self.genome[rowToMutate][colToMutate] = random.gauss(self.genome[rowToMutate][colToMutate], math.fabs(self.genome[rowToMutate][colToMutate]))

        if (self.genome[rowToMutate][colToMutate] > 1):
            self.genome[rowToMutate][colToMutate] = 1
        if (self.genome[rowToMutate][colToMutate] < -1):
            self.genome[rowToMutate][colToMutate] = -1
        
    def Print(self):
        print('[' + str(self.ID) + " " + str(self.fitness) + ']', end='')