from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK




class SIMULATION:

    def __init__(self):
        
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT()
        self.world = WORLD()
        self.robotId = self.robot.robotId
        #pyrosim.Prepare_To_Simulate(self.robotId)
        SIMULATION.Run(self)
    
    
    def Run(self): 
        for i in range(1,1000): 
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            time.sleep(1/900)
    def __del__(self):
        p.disconnect()
        