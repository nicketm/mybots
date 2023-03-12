import numpy as np


amplitude_BL = np.pi/4
frequency_BL = 10
phaseOffset_BL = 2 * np.pi/4
mottorcommandvector = np.linspace(0,2 * np.pi, 1000)


amplitude_FL = np.pi/4
frequency_FL = 10
phaseOffset_FL = 0

amplitude = np.pi/4
frequency = 10
phaseOffset = 0


frontLegSensorValues = np.zeros(1000)
backLegSensorValues = np.zeros(1000)


targetAngles_BL = np.array([])
for i in range(1, 1000): 
    targetAngles_BL = np.append(targetAngles_BL, amplitude_BL * np.sin(frequency_BL*mottorcommandvector[i]+phaseOffset_BL))

targetAngles_FL = np.array([])
for i in range(1, 1000): 
    targetAngles_FL = np.append(targetAngles_FL, amplitude_FL * np.sin(frequency_FL*mottorcommandvector[i]+phaseOffset_FL))

numberOfGenerations = 500
populationSize = 10

numSensorNeurons = 2
numMotorNeurons = 1

motorJointAngle = .5