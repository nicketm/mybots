import numpy as np


amplitude_BL = np.pi/4
frequency_BL = 10
phaseOffset_BL = 2 * np.pi/4
mottorcommandvector = np.linspace(0,2 * np.pi, 1000)


amplitude_FL = np.pi/4
frequency_FL = 10
phaseOffset_FL = 0

frontLegSensorValues = np.zeros(1000)
backLegSensorValues = np.zeros(1000)