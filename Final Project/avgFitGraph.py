import matplotlib.pyplot as plt 
from matplotlib import rc
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

rc('font',**{'family':'DejaVu Sans','sans-serif':['Helvetica']})
rc('text',usetex=True)

f = plt.figure() #adds a figure
panel = f.add_subplot(111) #creates drawing panel inside the figure 
panel.set_xlabel('Evolutionary time')
#panel.set_ylabel('Average Fitness')
plt.plot(fitness, label='Average Fitness') #plots data to the panel
plt.plot(tower, label = 'Tower distance')
#panel.set_ylim(0,7)
plt.legend()
plt.title(experiment)
plt.show() #shows the figure
f.savefig(experiment + '/' + experiment + '.png',bbox_inches='tight')