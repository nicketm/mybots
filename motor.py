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
        self.Prepare_To_Act()
        
    


    def Prepare_To_Act(self): 
        self.motorValues = np.array([])
        mottorcommandvector = np.linspace(0,2 * np.pi, 1000)
        for i in range(1000): 
            if self.jointName == b'Torso_BackLeg': 
                print('I AM HERE LOLOLOLOLOLOLOL')
                print(self.amplitude)
                self.amplitude = (c.amplitude * 1.5) / 2
                self.motorValues = np.append(self.motorValues, self.amplitude * np.sin(self.frequency * mottorcommandvector[i]+self.offset))
            else: 
                print(self.amplitude)
                self.motorValues = np.append(self.motorValues, self.amplitude * np.sin(self.frequency * mottorcommandvector[i]+self.offset))

            
    
    def Set_Value(self, robot, iteration): 
        pyrosim.Set_Motor_For_Joint(

            bodyIndex = robot,

            jointName = self.jointName,

            controlMode = p.POSITION_CONTROL,

            targetPosition = self.motorValues[iteration],

            maxForce = 200)
