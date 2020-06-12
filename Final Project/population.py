from individual import INDIVIDUAL
import numpy as np
import copy
import random

class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize
        

    def Initialize(self):
        for i in range(0,self.popSize):
            self.p[i] = INDIVIDUAL(i)


    def Print(self):
        for i in self.p:
            if (i in self.p):
                self.p[i].Print()
        print()
        
    def Evaluate(self, pb):
        for i in self.p:
            self.p[i].Start_Evaluation(pb)
        for i in self.p:
            self.p[i].Compute_Fitness()

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if(self.p[i].fitness < other.p[i].fitness):
                #if parent is less fit than child, replace
                self.p[i] = other.p[i]

    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

    def Copy_Best_From(self, other):
        highest = -np.inf #negative infinity
        bestI = 0
        for i in range(0, len(other.p)):
            if (other.p[i].fitness > highest):
                highest = other.p[i].fitness
                bestI = i

        best = copy.deepcopy(other.p[bestI])
        self.p[0] = best

    def Collect_Children_From(self, other):
        for i in range(1, self.popSize):
            winner = other.Winner_Of_Tournament_Selection()
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()
            #self.p[i] = copy.deepcopy(other.p[i])
    
    def Winner_Of_Tournament_Selection(self):
        #index of first parent
        p1 = random.randint(0, self.popSize-1)

        #make sure p1 and p2 are different
        parentsSame = True
        while parentsSame:
            p2 = random.randint(0, self.popSize-1)
            if (p2 != p1):
                parentsSame = False

        if (self.p[p1].fitness > self.p[p2].fitness):
            return self.p[p1]
        else:
            return self.p[p2]