import numpy as np 
import pyrosim.pyrosim as pyrosim
import random
import os 
import time



class SOLUTION: 
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights *2 - 1

    def Evaluate(self, guiOrDirect): 
        print('IN EVALUATE FOR SOME REASON')
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        #os.system("python simulate.py " + guiOrDirect)
        os_string = ("python3 simulate.py " + guiOrDirect + " " + str(self.myID) + " &")

        os.system(os_string)
        fitness_s = 'fitness' + str(self.myID) + '.txt'
        while not os.path.exists(fitness_s):
            time.sleep(0.01)
        f = open(fitness_s, "r")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()


    def Start_Simulation(self, guiOrDirect): 
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        #os.system("python simulate.py " + guiOrDirect)
        os_string = ("python3 simulate.py " + guiOrDirect + " " + str(self.myID) + " &")

        os.system(os_string)
    def Wait_For_Simulation_To_End(self): 
        fitness_s = 'fitness' + str(self.myID) + '.txt'
        while not os.path.exists(fitness_s):
            time.sleep(0.01)
        f = open(fitness_s, "r")
        self.fitness = float(f.read())
        #print(self.fitness)
        f.close()
        os.system('rm '+fitness_s)

    def Create_World(self): 
        length = 1
        width = 1
        height = 1
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[1,2,.5] , size=[length,width,height])

        pyrosim.End()

    def Generate_Body(self): 
        length = 1
        width = 1
        height = 1

        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
        pyrosim.End()

    def Generate_Brain(self): 
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")


        for currentRow in [0, 1, 2]: 
            for currentColumn in [0, 1]: 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self): 
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
    
    def Set_ID(self, id): 
        self.myID = id
        
