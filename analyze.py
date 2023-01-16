import numpy as np
import matplotlib.pyplot as mplib 


frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
backLegSensorValues = np.load('data/backLegSensorValues.npy')
print(frontLegSensorValues)
print(backLegSensorValues)
mplib.plot(frontLegSensorValues, label = 'frontLeg')
mplib.plot(backLegSensorValues, label = 'backLeg')
mplib.legend()
mplib.show()