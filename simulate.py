import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
frontLegSensorValues = np.zeros(100)
backLegSensorValues = np.zeros(100)

for i in range(1,100): 
    p.stepSimulation()
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(frontLegSensorValues[i])
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(1/60)
p.disconnect()
np.save('data/frontLegSensorValues', frontLegSensorValues)
np.save('data/backLegSensorValues', backLegSensorValues)
print(frontLegSensorValues)