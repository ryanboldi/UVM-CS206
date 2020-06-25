import matplotlib.pyplot as plt 
import pickle
import constants as c

experiment = '0-1000-5-1500'

f = open(experiment + '/' + experiment + 'fitness.p','rb')
fitness = pickle.load(f)
f.close()

g = open(experiment + '/' + experiment + 't.p','rb')
tower = pickle.load(g)
g.close()


print(fitness)

f = plt.figure() #adds a figure
panel = f.add_subplot(111) #creates drawing panel inside the figure 
plt.plot(fitness) #plots data to the panel
plt.plot(tower)
plt.show() #shows the figure