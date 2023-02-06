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
        pyrosim.Send_Cube(name="Box", pos=[0,20,0] , size=[4,20,.2])

        pyrosim.End()

    def Generate_Body(self): 
        length = 1
        width = 1
        height = 1
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,2] , size=[.7,2,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,2.0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,0] , size=[0.2, 1, 0.2])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,0] , size=[0.2, 1, 0.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-.5,.35,2], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5,-.9,0] , size=[1, 0.2, 0.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [.5,.35,2], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5,-.9,0] , size=[1, 0.2, 0.2])


        pyrosim.Send_Joint( name = "Torso_LefterLeg" , parent= "Torso" , child = "LefterLeg" , type = "revolute", position = [-.5,.3,2], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LefterLeg", pos=[-.5,.3,0] , size=[1, 0.2, 0.2])

        pyrosim.Send_Joint( name = "Torso_RighterLeg" , parent= "Torso" , child = "RighterLeg" , type = "revolute", position = [.5,.3,2], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RighterLeg", pos=[.5,.3,0] , size=[1, 0.2, 0.2])





        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-.5] , size=[.2, .2, 1])

        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-.5] , size=[.2, .2, 1])

        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,-.9,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-.5] , size=[.2, .2, 1])

        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,-.9,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-.5] , size=[.2, .2, 1])

        pyrosim.Send_Joint( name = "RighterLeg_RighterLowerLeg" , parent= "RighterLeg" , child = "RighterLowerLeg" , type = "revolute", position = [1,.3,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RighterLowerLeg", pos=[0,0,-.5] , size=[.2, .2, 1])

        pyrosim.Send_Joint( name = "LefterLeg_LefterLowerLeg" , parent= "LefterLeg" , child = "LefterLowerLeg" , type = "revolute", position = [-1,.3,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LefterLowerLeg", pos=[0,0,-.5] , size=[.2, .2, 1])
        
        pyrosim.End()
    def Generate_Brain(self): 
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LefterLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "RighterLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 11, linkName = "RighterLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "LefterLowerLeg")
        

        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "Torso_LefterLeg")
        pyrosim.Send_Motor_Neuron( name = 18 , jointName = "Torso_RighterLeg")
        pyrosim.Send_Motor_Neuron( name = 19 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 20 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 21 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 22 , jointName = "RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 23 , jointName = "LefterLeg_LefterLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 24 , jointName = "RighterLeg_RighterLowerLeg")




        for currentRow in range(c.numSensorNeurons): 
            for currentColumn in range(c.numMotorNeurons): 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+ c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self): 
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
    
    def Set_ID(self, id): 
        self.myID = id
        
