import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
RobotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
for i in range(1,1000): 
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()