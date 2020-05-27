from individual import INDIVIDUAL

class POPULATION:
    def __init__(self, popSize):
        self.p = {}

        for i in range(0,popSize):
            self.p[i] = INDIVIDUAL(i)


    def Print(self):
        for i in self.p:
            self.p[i].Print()
        print()
        
    def Evaluate(self):
        for i in self.p:
            self.p[i].Start_Evaluation(True)
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