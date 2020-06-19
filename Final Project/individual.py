import random
import pyrosim
import math
import numpy as np
from robot import ROBOT
from tower import TOWER
import constants as c

class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = np.random.rand(14,6) *2 -1
        self.fitness = 0
    
    def Start_Evaluation(self, pb, tower_y):
        self.pb = pb
        self.sim = pyrosim.Simulator( play_paused=True, eval_time=500, play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        self.tower = TOWER(self.sim, tower_y)
        self.sim.assign_collision("tower", "tower")
        self.sim.assign_collision("tower", "robot")
        self.sim.start()
        

    def Compute_Fitness(self):
        self.sim.wait_to_finish()

        #gets x,y,z coord of individual's red cylinder.
        y = self.sim.get_sensor_data(sensor_id=self.robot.P4 , svi = 1)

        fallData = self.sim.get_sensor_data(sensor_id=self.tower.fallSensor, svi=2)

        #print(fallData)
        #if tower z is smaller than start posititon
        #if (not(self.pb)):
            #print(fallData)
            #print(c.TL + (c.TW/2))
        
        if (fallData[-1] < (0.9 * (c.TL + (c.TW/2)))):
            self.fitness = 20
        else:
            self.fitness = y[-1]
             
        #self.fitness = y[-1] #gets last element in y array (last y pos)
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