import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c




class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.amplitude = c.amplitude * 2
        self.frequency = c.frequency 
        self.offset = c.phaseOffset
        
    def Set_Value(self, robot, desiredAngle): 
        pyrosim.Set_Motor_For_Joint(

            bodyIndex = robot,

            jointName = self.jointName,

            controlMode = p.POSITION_CONTROL,

            targetPosition = desiredAngle,

            maxForce = 200)
