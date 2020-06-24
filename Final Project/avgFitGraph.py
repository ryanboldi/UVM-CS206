import matplotlib.pyplot as plt 
import pickle
import constants as c

f = open('0-2K-50fitness.p','rb')
fitness = pickle.load(f)
f.close()

print(fitness)

f = plt.figure() #adds a figure
panel = f.add_subplot(111) #creates drawing panel inside the figure 
plt.plot(fitness) #plots data to the panel
plt.show() #shows the figure