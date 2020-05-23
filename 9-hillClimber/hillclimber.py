import pyrosim
import matplotlib.pyplot as plt 
import random
import pickle
import copy

from robot import ROBOT
from individual import INDIVIDUAL

parent = INDIVIDUAL()
parent.Evaluate(False)
print(parent.fitness)

for i in range(0,100):
    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate(True)
    print('[g: ',i,'] [pw: ',parent.genome,'] [p: ',parent.fitness,'] [c: ',child.fitness,']')
    if (child.fitness > parent.fitness):
        child.Evaluate(False) #draw all the good children
        parent = child

        #save parent to file
        f=open('robot.p','wb')
        pickle.dump(parent, f)
        f.close()
        

#sensorData = sim.get_sensor_data(sensor_id = P2)
#print(sensorData)

#f = plt.figure() #adds a figure
#panel = f.add_subplot(111) #creates drawing panel inside the figure 
#plt.plot(sensorData) #plots data to the panel
#panel.set_ylim(-3,3)
#plt.show() #shows the figure