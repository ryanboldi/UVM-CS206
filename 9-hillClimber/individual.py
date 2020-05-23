import random
import pyrosim
import math
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self):
        self.genome = random.random()*2 -1 
        self.fitness = 0
    
    #pb -> play blind or no
    def Evaluate(self, pb):
        sim = pyrosim.Simulator( play_paused=False, eval_time=500, play_blind=pb)
        robot = ROBOT(sim, self.genome)

        sim.start()
        sim.wait_to_finish()

        #gets x,y,z coord of individual's red cylinder.
        y = sim.get_sensor_data(sensor_id=robot.P4 , svi = 1)

        self.fitness = y[-1] #gets last element in y array (last y pos)

    def Mutate(self):
        #new random value close to parent's random value
        #Standard deviation is |self.genome| to make the mutate take 
        # larger steps the larger the genome is
        self.genome = random.gauss(self.genome, math.fabs(self.genome))
        