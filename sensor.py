import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c



class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(3000)

    def Get_Value(self, iteration):
        self.values[iteration] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        