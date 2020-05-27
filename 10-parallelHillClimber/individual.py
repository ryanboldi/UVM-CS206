import random
import pyrosim
import math
import numpy as np
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = np.random.random(4) * 2 - 1 
        self.fitness = 0
    
    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator( play_paused=False, eval_time=500, play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()

        #gets x,y,z coord of individual's red cylinder.
        y = self.sim.get_sensor_data(sensor_id=self.robot.P4 , svi = 1)

        self.fitness = y[-1] #gets last element in y array (last y pos)
        del self.sim

    def Mutate(self):
        geneToMutate = random.randint(0,3)
        #new random value close to parent's random value
        #Standard deviation is |self.genome| to make the mutate take 
        # larger steps the larger the genome is
        self.genome[geneToMutate] = random.gauss(self.genome[geneToMutate], math.fabs(self.genome[geneToMutate]))
        
    def Print(self):
        print('[' + str(self.ID) + " " + str(self.fitness) + ']', end='')