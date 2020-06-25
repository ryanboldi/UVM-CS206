import matplotlib.pyplot as plt 
import pickle
import constants as c

f = open('5-10-50-1600/5-10-50-1600fitness.p','rb')
fitness = pickle.load(f)
f.close()

g = open('5-10-50-1600/5-10-50-1600t.p','rb')
tower = pickle.load(g)
g.close()


print(fitness)

f = plt.figure() #adds a figure
panel = f.add_subplot(111) #creates drawing panel inside the figure 
plt.plot(fitness) #plots data to the panel
plt.plot(tower)
plt.show() #shows the figure