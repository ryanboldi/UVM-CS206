import matplotlib.pyplot as plt 
import pickle
import constants as c

experiment = '3000-6000-15-1500'

f = open(experiment + '/' + experiment + 'fitness.p','rb')
fitness = pickle.load(f)
f.close()

g = open(experiment + '/' + experiment + 't.p','rb')
tower = pickle.load(g)
g.close()


print(fitness)

f = plt.figure() #adds a figure
panel = f.add_subplot(111) #creates drawing panel inside the figure 
panel.set_xlabel('Evolutionary time')
#panel.set_ylabel('Average Fitness')
plt.plot(fitness, label='Average Fitness') #plots data to the panel
plt.plot(tower, label = 'Tower distance')
plt.legend()
plt.show() #shows the figure