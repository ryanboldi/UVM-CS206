from individual import INDIVIDUAL
import pickle
import constants as c

f = open('500-1k-50-1250/500-1K-50-1250best.p','rb')
best = pickle.load(f)
f.close()

best.Start_Evaluation(False, c.Max_dist)
best.Compute_Fitness()
print(best.fitness)