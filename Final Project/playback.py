from individual import INDIVIDUAL
import pickle

f = open('robot.p','rb')
best = pickle.load(f)
f.close()

best.Start_Evaluation(False)
best.Compute_Fitness()
print(best.fitness)