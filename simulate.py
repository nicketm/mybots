import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from simulation import SIMULATION



simulation = SIMULATION()
"""
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)


targetAngles_BL = np.array([])
for i in range(1, 1000): 
    targetAngles_BL = np.append(targetAngles_BL, c.amplitude_BL * np.sin(c.frequency_BL*c.mottorcommandvector[i]+c.phaseOffset_BL))

targetAngles_FL = np.array([])
for i in range(1, 1000): 
    targetAngles_FL = np.append(targetAngles_FL, c.amplitude_FL * np.sin(c.frequency_FL*c.mottorcommandvector[i]+c.phaseOffset_FL))

np.save('data/targetAngles_BL', targetAngles_BL)
np.save('data/targetAngles_FL', targetAngles_FL)

for i in range(1,1000): 
    p.stepSimulation()
    c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b'Torso_BackLeg',

    controlMode = p.POSITION_CONTROL,

    targetPosition = targetAngles_BL[i],

    maxForce = 200)


    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b'Torso_FrontLeg',

    controlMode = p.POSITION_CONTROL,

    targetPosition = targetAngles_FL[i],

    maxForce = 200)


    time.sleep(1/1500)
p.disconnect()
np.save('data/frontLegSensorValues', c.frontLegSensorValues)
np.save('data/backLegSensorValues', c.backLegSensorValues)
"""