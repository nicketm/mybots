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
        print(self.jointName)
        self.amplitude = c.amplitude * 1.5 
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        #self.Prepare_To_Act()
        
    


    

            
    
    def Set_Value(self, robot, desiredAngle): 
        pyrosim.Set_Motor_For_Joint(

            bodyIndex = robot,

            jointName = self.jointName,

            controlMode = p.POSITION_CONTROL,

            targetPosition = desiredAngle,

            maxForce = 200)
