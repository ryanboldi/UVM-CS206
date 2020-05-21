import pyrosim
import matplotlib.pyplot as plt 
import random
from robot import ROBOT


for i in range(0,10):
    sim = pyrosim.Simulator( play_paused=False, eval_time=300)
    robot = ROBOT(sim, random.random()*2 - 1)

    sim.start()
    sim.wait_to_finish()

#sensorData = sim.get_sensor_data(sensor_id = P2)
#print(sensorData)

#f = plt.figure() #adds a figure
#panel = f.add_subplot(111) #creates drawing panel inside the figure 
#plt.plot(sensorData) #plots data to the panel
#panel.set_ylim(-3,3)
#plt.show() #shows the figure