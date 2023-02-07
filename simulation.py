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
import sys





class SIMULATION:

    def __init__(self, directOrGui, solutionID):
        self.directOrGui = directOrGui
        if directOrGui == 'DIRECT': 
            physicsClient = p.connect(p.DIRECT)
        else: 
            physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT(solutionID)
        self.world = WORLD()
        self.robotId = self.robot.robotId
        #pyrosim.Prepare_To_Simulate(self.robotId)
        SIMULATION.Run(self)
    
    
    def Run(self): 
        for i in range(1,5000): 
            p.stepSimulation()
            ballLoc = self.world.get_location()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            self.robot.saveBall(ballLoc)
            if self.directOrGui == 'GUI': 
                time.sleep(1/4000)
    def __del__(self):
        p.disconnect()
    def Get_Fitness(self): 
        self.robot.Get_Fitness()
        
