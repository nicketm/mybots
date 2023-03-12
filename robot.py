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
from world import WORLD

class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        filename = "body" + str(self.solutionID) + ".urdf"
        self.robotId = p.loadURDF(filename)
        #self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        #self.world = WORLD()
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
        deletestring = "rm brain" + str(solutionID) + ".nndf"
        os.system(deletestring)
        self.ballLocation = 0
    
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
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * .3
                self.motors[bytes(jointName, 'utf-8')].Set_Value(self.robotId, desiredAngle)


    def Think(self): 
        self.nn.Update()
       # self.nn.Print()

    def Get_Fitness(self): 
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = abs(basePosition[0])
        yPosition = basePosition[1]
        optimized = yPosition
        if xPosition < -2 or xPosition > 3: 
            optimized = yPosition - 10 
        if self.ballLocation < .35: 
            optimized = optimized -50
        #cubeloc = self.world.get_location(self.world.worldSDF)
        temp_s = 'tmp' + str(self.solutionID) + '.txt'
        fitness_s = 'fitness' + str(self.solutionID) + '.txt'
        f = open(temp_s, 'w')
        f.write(str(xPosition))
        f.close()
        os.system('mv ' +  temp_s + ' ' + fitness_s)
        exit()


