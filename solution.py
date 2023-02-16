import numpy as np 
import pyrosim.pyrosim as pyrosim
import random
import os 
import time
import constants as c



class SOLUTION: 
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.numlinks = np.random.randint(2, 10) 
        print('numlinks', self.numlinks)
        self.numjoints = self.numlinks - 1
        self.weights = np.random.rand(self.numlinks, self.numjoints)
        self.weights = self.weights * 2 - 1
        self.sensor_ind = self.create_sensor_ind()
        self.numsensor = len(self.sensor_ind)
        #self.numlinks = 2 
        print('sensor ind', self.sensor_ind)


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
        pyrosim.End()


    def Generate_Body(self): 
        sizex =  np.random.uniform(.5, 1.5)
        sizey =  np.random.uniform(.5, 1.5)
        sizez =  np.random.uniform(.5, 1.5)
        pyrosim.Start_URDF("body.urdf")

        # start link
        pyrosim.Send_Cube(name="Link" + str(0), pos=[0,0,1.25] , size=[sizex, sizey, sizez], color = 'blue')
        JA = self.generate_joint_axis()
        pyrosim.Send_Joint( name = "Link" + str(0) + "_Link" + str(1) , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1.25], jointAxis = JA)
        poslink = 0
        posjoint = 0
        for i in range(1, self.numlinks): 
            sizex =  np.random.uniform(.75, 1.25)
            sizey =  np.random.uniform(.75, 1.25)
            sizez =  np.random.uniform(.75, 1.25)
            poslink = sizex 
            posjoint = sizex
            if i in self.sensor_ind: 
                pyrosim.Send_Cube(name="Link" + str(i), pos=[poslink,0,0] , size=[sizex, sizey, sizez], color = 'green')
            else: 
                pyrosim.Send_Cube(name="Link" + str(i), pos=[poslink,0,0] , size=[sizex, sizey, sizez], color = 'blue')
            if i != self.numlinks -1: 
                JA = self.generate_joint_axis()
                pyrosim.Send_Joint( name = "Link" + str(i) + "_Link" + str(i + 1) , parent= "Link" + str(i) , child = "Link" + str(i + 1) , type = "revolute", position = [posjoint,0,0], jointAxis = JA)


        pyrosim.End()
    def Generate_Brain(self): 
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
        sensorcnt = 0
        for i in range(len(self.sensor_ind)):
            pyrosim.Send_Sensor_Neuron(name = sensorcnt , linkName = "Link"+ str(self.sensor_ind[i]))
            sensorcnt += 1

        for i in range(len(self.sensor_ind)): 
            if self.sensor_ind[i] + 1 < self.numlinks:    
                pyrosim.Send_Motor_Neuron( name = sensorcnt , jointName = "Link" + str(self.sensor_ind[i]) + "_Link" + str(self.sensor_ind[i] + 1))
                sensorcnt += 1
        
        for currentRow in range(len(self.sensor_ind)): 
            for currentColumn in range(len(self.sensor_ind) - 1): 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+ self.numsensor , weight = self.weights[currentRow][currentColumn] )
    

    



    def Mutate(self): 
        print('IN MUTATE')
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
    
    def Set_ID(self, id): 
        self.myID = id

    def create_sensor_ind(self): 
        length = np.random.randint(1, self.numlinks)
        lst = []
        for i in range(length): 
            lst.append(np.random.randint(2, self.numlinks))
        unqlst = list(set(lst))
        return unqlst
        
    def generate_joint_axis(self): 
        ind = np.random.randint(0, 3)
        lst = ["1 0 0", "0 1 0", "0 0 1"]
        return lst[ind]