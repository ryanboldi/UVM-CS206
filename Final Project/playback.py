from individual import INDIVIDUAL
import pickle
import constants as c

f = open('0-2K-50best.p','rb')
best = pickle.load(f)
f.close()

best.Start_Evaluation(False, c.Max_dist)
best.Compute_Fitness()
print(best.fitness)