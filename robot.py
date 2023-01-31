from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
        deletestring = "rm brain" + str(solutionID) + ".nndf"
        os.system(deletestring)
    
    def Prepare_To_Sense(self): 
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, iteration): 
        for sensor in self.sensors: 
            self.sensors[sensor].Get_Value(iteration)

    def Prepare_To_Act(self): 
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices: 
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, desiredAngle): 
        for neuronName in self.nn.Get_Neuron_Names():
            #print(self.motors)
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                #print(jointName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointAngle
                self.motors[bytes(jointName, 'utf-8')].Set_Value(self.robotId, desiredAngle)
                #print(neuronName)
                #print(jointName)
                #print(desiredAngle)


    def Think(self): 
        self.nn.Update()
       # self.nn.Print()

    def Get_Fitness(self): 
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        #print(stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        #print(positionOfLinkZero)
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        #print(xCoordinateOfLinkZero)
        temp_s = 'tmp' + str(self.solutionID) + '.txt'
        fitness_s = 'fitness' + str(self.solutionID) + '.txt'
        f = open(temp_s, 'w')
        f.write(str(xCoordinateOfLinkZero))
        os.system('mv ' +  temp_s + ' ' + fitness_s)
        exit()



