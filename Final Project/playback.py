from individual import INDIVIDUAL
import pickle
import constants as c

experiment = '0-600-100-1500'

f = open(experiment + '/' + experiment + 'best.p','rb')
best = pickle.load(f)
f.close()

best.Start_Evaluation(False, c.Max_dist)
best.Compute_Fitness()
print(best.fitness)