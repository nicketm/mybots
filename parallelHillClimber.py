
from solution import SOLUTION
import constants as c
import copy 
import os


class PARALLEL_HILL_CLIMBER: 
    def __init__(self):
        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')
        self.nextAvailableID = 0
        self.parents = {}
        for parentID in range(c.populationSize):
            parent = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[parentID] = parent
        #self.parent = SOLUTION()
        #print(self.parents)

    def Spawn(self): 
        self.children = {}
        for parent in self.parents: 
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            #print(self.children[parent])
        #self.child = copy.deepcopy(self.parent)
        #self.child.Set_ID(self.nextAvailableID)
        #self.nextAvailableID += 1
    def Mutate(self): 
        #print('in Mutate')
        for child in self.children: 
            self.children[child].Mutate()
    def Evolve(self): 
        self.Evaluate(self.parents)
        

        #self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()


    def Select(self): 
        for key in self.parents: 
            print(self.parents[key].fitness)
            print(self.children[key].fitness)
            if self.parents[key].fitness > self.children[key].fitness: 
                self.parents[key] = self.children[key]
        
        
        #if self.parent.fitness > self.child.fitness: 
        #    print('CHILD BETTER THAN PARENT')
        #    self.parent = self.child
    
    def Print(self): 
        for key in self.parents: 
            print('\n')
            print('parent fitness: ', self.parents[key].fitness, 'child fitness: ', self.children[key].fitness)
            print('\n')
    def Show_Best(self): 
        lf = 100000000
        keyid = -1
        for parent in self.parents: 
            if self.parents[parent].fitness < lf: 
                lf = self.parents[parent].fitness
                keyid = parent
        
        self.parents[parent].Start_Simulation("GUI")

        #self.parent.Evaluate("GUI")
        pass

    def Evaluate(self, solutions):
        for parent in solutions: 
            #self.parents[parent].Evaluate("GUI")
            solutions[parent].Start_Simulation("DIRECT")
        for parent in solutions: 
            solutions[parent].Wait_For_Simulation_To_End()

