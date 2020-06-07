import pyrosim
import matplotlib.pyplot as plt 
import random
import pickle
import copy

from robot import ROBOT
from individual import INDIVIDUAL
from population import POPULATION

from multiprocessing import Lock

import constants as c

from environments import ENVIRONMENTS

envs = ENVIRONMENTS()

#Load = False

parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp=False, pb=True)
print('Gen 0: ', end='')
parents.Print()


#if (Load):
#    f = open('robot.p','rb')
#    best = pickle.load(f)
#    f.close()
#    parents.p[0] = best

for g in range(1,c.numGens):
     children = POPULATION(c.popSize)
     children.Fill_From(parents)
     children.Evaluate(envs, pp=False, pb=True)
     print('Gen '+str(g)+': ', end='')
     children.Print()
     parents = children


best = copy.deepcopy(parents.p[0])

#save parent to file
f=open('robot.p','wb')
pickle.dump(best, f)
f.close()

#play best creature
for e in envs.envs:
  parents.p[0].Start_Evaluation(envs.envs[e], pp=True, pb = False)


#    children = copy.deepcopy(parents)
#    children.Mutate()
#    children.Evaluate(True)
#    parents.ReplaceWith(children)
#    print(g, end=' ')
#    parents.Print()

#parents.Evaluate(False)


#parent = INDIVIDUAL()
#parent.Evaluate(True)
#print(parent.fitness)

#for i in range(0,100):
#    child = copy.deepcopy(parent)
#    child.Mutate()
#    child.Evaluate(True)
#    print('[g: ',i,'] [pw: ',parent.genome,'] [p: ',parent.fitness,'] [c: ',child.fitness,']')
#    if (child.fitness > parent.fitness):
#        child.Evaluate(True) #draw all the good children
#        parent = child

        
        

#sensorData = sim.get_sensor_data(sensor_id = P2)
#print(sensorData)

#f = plt.figure() #adds a figure
#panel = f.add_subplot(111) #creates drawing panel inside the figure 
#plt.plot(sensorData) #plots data to the panel
#panel.set_ylim(-3,3)
#plt.show() #shows the figure