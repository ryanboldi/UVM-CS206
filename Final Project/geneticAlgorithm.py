import pyrosim
import matplotlib.pyplot as plt 
import random
import pickle
import copy

import constants as c
from robot import ROBOT
from individual import INDIVIDUAL
from population import POPULATION

from multiprocessing import Lock

Load = False
popSize = 50

avgFitnesses = []

t = c.Min_dist

parents = POPULATION(popSize)
parents.Initialize()

if (Load):
    f = open('parents1.p','rb')
    parents  = pickle.load(f)
    f.close()
    #parents.p[0] = best

parents.Evaluate(True, t)
print('Gen 0: ', end='')
parents.Print()


#count = 0

for g in range(1,c.totGens):
    if (g == c.gens):
        t = c.Max_dist
    #if (count == c.inc_time):
     #   count = 0
      #  if (t+c.gen_incremement <= c.Max_dist):
       #     t += c.gen_incremement

    children = POPULATION(popSize)
    children.Fill_From(parents)
    children.Evaluate(True, t)

    if (children.p[0].fitness == 20):
        if (t+c.gen_incremement <= c.Max_dist):
            print("TOWER MOVED")
            t += c.gen_incremement
        else:
            t= c.Max_dist

    print('Gen '+str(g)+': ', end='')
    children.Print()
    #print('tower distance:' + str(t))
    avgFitnesses.append(children.get_avg_fitness())
    parents = children

    #scount+=1

best = copy.deepcopy(parents.p[0])

#save parent to file
f=open('0-2K-50best.p','wb')#0 pretrain, 6K on max dist, 100 pop best creature
pickle.dump(parents.p[0], f)
f.close()


#save avg fitness of every gen to file
f=open('0-2K-50fitness.p','wb')#0 pretrain, 6K on max dist, 100 pop
pickle.dump(avgFitnesses, f)
f.close()

#play best creature
parents.p[0].Start_Evaluation(False, t)
parents.p[0].Compute_Fitness()


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