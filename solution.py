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


        pyrosim.Send_Joint( name = "Torso_LeftFrontOne" , parent= "Torso" , child = "LeftFrontOne" , type = "revolute", position = [-.5,.75,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftFrontOne", pos=[0,0,0] , size=[.5, .5, .5])
        pyrosim.Send_Joint( name = "Torso_LeftFrontTwo" , parent= "Torso" , child = "LeftFrontTwo" , type = "revolute", position = [-.5,.7,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftFrontTwo", pos=[0,0,0] , size=[.5, .5, .5])


        pyrosim.Send_Joint( name = "Torso_LeftBackOne" , parent= "Torso" , child = "LeftBackOne" , type = "revolute", position = [-.5,-.75,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftBackOne", pos=[0,0,0] , size=[.5, .5, .5])
        pyrosim.Send_Joint( name = "Torso_LeftBackTwo" , parent= "Torso" , child = "LeftBackTwo" , type = "revolute", position = [-.5,-.7,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftBackTwo", pos=[0,0,0] , size=[.5, .5, .5])


        pyrosim.Send_Joint( name = "Torso_RightFrontOne" , parent= "Torso" , child = "RightFrontOne" , type = "revolute", position = [.5,.75,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightFrontOne", pos=[0,0,0] , size=[.5, .5, .5])
        pyrosim.Send_Joint( name = "Torso_RightFrontTwo" , parent= "Torso" , child = "RightFrontTwo" , type = "revolute", position = [.5,.7,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightFrontTwo", pos=[0,0,0] , size=[.5, .5, .5])


        pyrosim.Send_Joint( name = "Torso_RightBackOne" , parent= "Torso" , child = "RightBackOne" , type = "revolute", position = [.5,-.75,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightBackOne", pos=[0,0,0] , size=[.5, .5, .5])
        pyrosim.Send_Joint( name = "Torso_RightBackTwo" , parent= "Torso" , child = "RightBackTwo" , type = "revolute", position = [.5, -.75,1.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightBackTwo", pos=[0,0,0] , size=[.5, .5, .5])


        
        pyrosim.End()
    def Generate_Brain(self): 
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftFrontOne")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightFrontOne")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftFrontTwo")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightFrontTwo")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LeftBackOne")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "RightBackOne")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftBackTwo")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightBackTwo")
        
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_LeftFrontOne")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_RightFrontTwo")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftFrontTwo")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightFrontOne")

        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_LeftBackOne")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Torso_RightBackTwo")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_LeftBackTwo")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Torso_RightBackOne")
        
        for currentRow in range(c.numSensorNeurons): 
            for currentColumn in range(c.numMotorNeurons): 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+ c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )
    

    



    def Mutate(self): 
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
    
    def Set_ID(self, id): 
        self.myID = id
        
