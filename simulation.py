from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c




class SIMULATION:

    def __init__(self):
        
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT()
        self.world = WORLD()
        #self.robotId = p.loadURDF("body.urdf")
        #pyrosim.Prepare_To_Simulate(self.robotId)
        