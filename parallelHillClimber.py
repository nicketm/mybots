
from solution import SOLUTION
import constants as c
import copy 
import os


class PARALLEL_HILL_CLIMBER: 
    def __init__(self):
        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')
        os.system('rm body*.urdf')
        self.nextAvailableID = 0
        self.parents = {}
        for parentID in range(c.populationSize):
            parent = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[parentID] = parent
        #self.parent = SOLUTION()
        #print(self.parents)
        self.fitness_w = {}
        for i in range(10): 
             self.fitness_w[i] = []

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
        bodynum = 0
        for child in self.children: 
            self.children[child].Mutate(bodynum)
            bodynum += 1
    def Evolve(self): 
        self.Evaluate(self.parents, 1)
        

        #self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            print(' GENERATION: ', currentGeneration)
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, 0)
        self.Select()
        self.Print()


    def Select(self): 
        for key in self.parents: 
            if self.parents[key].fitness < self.children[key].fitness: 
                self.parents[key] = self.children[key]
                self.fitness_w[key].append(self.children[key].fitness)
            else: 
                self.fitness_w[key].append(self.parents[key].fitness)

    
    def Print(self): 
        for key in self.parents: 
            print('\n')
            print('parent fitness: ', self.parents[key].fitness, 'child fitness: ', self.children[key].fitness)
            print('\n')
    def Show_Best(self): 
        print('in show best')
        lf = 0
        keyid = 0
        print(self.parents)
        for parent in self.parents: 
            if self.parents[parent].fitness > lf: 
                lf = self.parents[parent].fitness
                keyid = parent
        print(self.parents[keyid].fitness)
        print(keyid)
        self.parents[keyid].Continue_Simulation("GUI")

        #self.parent.Evaluate("GUI")
        fitness_graph = 'fitness_graph.txt'
        with open(fitness_graph, 'w') as f:
            # Loop through dictionary values and write to file
            for value in self.fitness_w.values():
                f.write(f"{value}\n\n")
        pass
    def Show_Worst(self): 
        print('in show worst')
        lf = 10000000
        keyid = -1
        for parent in self.parents: 
            if self.parents[parent].fitness < lf: 
                lf = self.parents[parent].fitness
                keyid = parent
        
        self.parents[keyid].Continue_Simulation("GUI")

        #self.parent.Evaluate("GUI")
        pass
    def Evaluate(self, solutions, parentbool):
        if parentbool == 1: 
            for parent in solutions: 
                #self.parents[parent].Evaluate("GUI")
                solutions[parent].Start_Simulation("DIRECT")
            for parent in solutions: 
                solutions[parent].Wait_For_Simulation_To_End()
        else: 
            for parent in solutions: 
                #self.parents[parent].Evaluate("GUI")
                solutions[parent].Continue_Simulation("DIRECT")
            for parent in solutions: 
                solutions[parent].Wait_For_Simulation_To_End()


