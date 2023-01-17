from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c


class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
    
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

    def Act(self,iteration): 
        for motor in self.motors: 
            self.motors[motor].Set_Value(self.robotId, iteration)


