import pyrosim
import matplotlib.pyplot as plt 
import random
from robot import ROBOT
from individual import INDIVIDUAL


for i in range(0,10):
    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)


#sensorData = sim.get_sensor_data(sensor_id = P2)
#print(sensorData)

#f = plt.figure() #adds a figure
#panel = f.add_subplot(111) #creates drawing panel inside the figure 
#plt.plot(sensorData) #plots data to the panel
#panel.set_ylim(-3,3)
#plt.show() #shows the figure