import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c




class WORLD:

    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        self.worldSDF = p.loadSDF("world.sdf")
        #self.get_location()
    def get_location(self, world): 
        location = p.getBasePositionAndOrientation(world[-1])
    