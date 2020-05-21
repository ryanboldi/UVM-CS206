import random
import pyrosim
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self):
        self.genome = random.random()*2 -1 
        self.fitness = 0
    
    def Evaluate(self):
        sim = pyrosim.Simulator( play_paused=False, eval_time=500)
        robot = ROBOT(sim, random.random()*2 - 1)

        sim.start()
        sim.wait_to_finish()

        #gets x,y,z coord of individual's red cylinder.
        y = sim.get_sensor_data(sensor_id=robot.P4 , svi = 1)

        self.fitness = y[-1] #gets last element in y array (last y pos)