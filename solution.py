import numpy as np 
import pyrosim.pyrosim as pyrosim
import random
import os 
import time
import constants as c



class SOLUTION: 
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, guiOrDirect): 
        print('IN EVALUATE FOR SOME REASON')
        self.Create_World()
        self.Generate_Body()
        #self.Generate_Brain()
        #os.system("python simulate.py " + guiOrDirect)
        os_string = ("python3 simulate.py " + guiOrDirect + " " + str(self.myID) + " 2&>1 &")

        os.system(os_string)
        fitness_s = 'fitness' + str(self.myID) + '.txt'
        while not os.path.exists(fitness_s):
            time.sleep(0.01)
        f = open(fitness_s, "r")
        self.fitness = float(f.read())
        #print(self.fitness)
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
        #pyrosim.Send_Cube(name="Box", pos=[0,0,0] , size=[20,4,.2])
        #pyrosim.Send_Cube(name="Box", pos=[-3,0,0] , size=[1,1,1])
        pyrosim.Send_Cube(name="Box", pos=[-5,-1,0] , size=[length,width,height])
        pyrosim.Send_Cube(name="Box", pos=[-5,5,0] , size=[length,width,height])
        pyrosim.Send_Cube(name="Box", pos=[-5,10,0] , size=[length,width,height])
        pyrosim.Send_Cube(name="Box", pos=[-5,15,0] , size=[length,width,height])
        pyrosim.Send_Cube(name="Box", pos=[-10,0,0] , size=[1,1,1])
        pyrosim.Send_Cube(name="Box", pos=[-10,4,0] , size=[1,1,1])

        pyrosim.End()


    def Generate_Body(self): 
        length = 1
        width = 1
        height = 1
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,2] , size=[.7,2,height])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-.5,.35,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0,-.9,0] , size=[.5, .5, .5])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [.5,.35,1.5], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0,-.9,0] , size=[.5, .5, .5])


        pyrosim.Send_Joint( name = "Torso_LefterLeg" , parent= "Torso" , child = "LefterLeg" , type = "revolute", position = [-.5,.3,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LefterLeg", pos=[0,.3,0] , size=[.5, .5, .5])

        pyrosim.Send_Joint( name = "Torso_RighterLeg" , parent= "Torso" , child = "RighterLeg" , type = "revolute", position = [.5,.3,1.5], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RighterLeg", pos=[0,.3,0] , size=[.5, .5, .5])


        
        pyrosim.End()
    def Generate_Brain(self): 
            pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
            pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
            pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftLeg")
            pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightLeg")
            pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LefterLeg")
            pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RighterLeg")
            
            pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_LeftLeg")
            pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_RightLeg")
            pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_LefterLeg")
            pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_RighterLeg")
    

    



    def Mutate(self): 
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
    
    def Set_ID(self, id): 
        self.myID = id
        
