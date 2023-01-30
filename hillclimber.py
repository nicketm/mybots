
from solution import SOLUTION
import constants as c
import copy 


class HILL_CLIMBER: 
    def __init__(self):
        self.parent = SOLUTION()

    def Spawn(self): 
        self.child = copy.deepcopy(self.parent)
    
    def Evolve(self): 
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()
        self.Print()
    

    def Mutate(self): 
        self.child.Mutate()


    def Select(self): 
        if self.parent.fitness > self.child.fitness: 
            print('CHILD BETTER THAN PARENT')
            self.parent = self.child
    
    def Print(self): 
        print('parent fitness: ', self.parent.fitness, 'child fitness: ', self.child.fitness)

    def Show_Best(self): 
        self.parent.Evaluate("GUI")