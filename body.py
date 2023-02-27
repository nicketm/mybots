import numpy as np 
import pyrosim.pyrosim as pyrosim
import random
import os 
import time
import constants as c


class BODY: 
    def __init__(self, ID, weights, joints, directions, jointaxis, sizes, sensor_ind, numlinks):
        self.ID = ID
        self.sensor_ind = sensor_ind
        self.weights = weights
        self.joints = joints
        self.directions = directions
        self.jointAxis = jointaxis
        self.sizes = sizes
        self.numlinks = numlinks
        #print(self.joints)




    def Generate_Body(self): 
        print(self.sizes)
        sizex =  self.sizes[0][0]
        sizey =  self.sizes[0][1]
        sizez =  self.sizes[0][2]
        filename = "body" + str(self.ID) + ".urdf"
        pyrosim.Start_URDF(filename)

        # start link
        pyrosim.Send_Cube(name="Link" + str(0), pos=[0,0,2] , size=[sizex, sizey, sizez], color = 'blue')
        for i in range(1, self.numlinks): 
            sizex =  self.sizes[i][0]
            sizey =  self.sizes[i][1]
            sizez =  self.sizes[i][2]
            if self.directions[i][3] == 'x':
                if i in self.sensor_ind: 
                    pyrosim.Send_Cube(name="Link" + str(i), pos=[sizex - .2, 0, 2] , size=self.sizes[i], color = 'green')
                else: 
                    pyrosim.Send_Cube(name="Link" + str(i), pos=[sizex - .2, 0, 2] , size=self.sizes[i], color = 'blue')
                for j in self.joints: 
                    print(j)
                    if j[1] == i: 
                        pyrosim.Send_Joint( name = "Link" + str(j[0]) + "_Link" + str(i) , parent= "Link" + str(j[0]) , child = "Link" + str(i) , type = "revolute", position = self.directions[i], jointAxis = self.jointAxis[(j[0], i)])
                        break 
            if self.directions[i][3] == 'y':
                if i in self.sensor_ind: 
                    pyrosim.Send_Cube(name="Link" + str(i), pos=[0, sizey - .2, 2] , size=self.sizes[i], color = 'green')
                else: 
                    pyrosim.Send_Cube(name="Link" + str(i), pos=[0, sizey - .2, 2] , size=self.sizes[i], color = 'blue')
                print(' ABOUT TO LOOP THROUGH SELF JOINTS Y')
                print(self.joints)
                for j in self.joints: 
                    print(j)
                    if j[1] == i: 
                        pyrosim.Send_Joint( name = "Link" + str(j[0]) + "_Link" + str(i) , parent= "Link" + str(j[0]) , child = "Link" + str(i) , type = "revolute", position = self.directions[i], jointAxis = self.jointAxis[(j[0], i)])
                        break
            if self.directions[i][3] == 'z':
                if i in self.sensor_ind: 
                    pyrosim.Send_Cube(name="Link" + str(i), pos=[0, 0, sizez + 1.8]  , size=self.sizes[i], color = 'green')
                else: 
                    pyrosim.Send_Cube(name="Link" + str(i), pos=[0, 0, sizez + 1.8]  , size=self.sizes[i], color = 'blue')
                print(' ABOUT TO LOOP THROUGH SELF JOINTS Z')
                print(self.joints)
                for j in self.joints: 
                    print(j)
                    if j[1] == i: 
                        pyrosim.Send_Joint( name = "Link" + str(j[0]) + "_Link" + str(i) , parent= "Link" + str(j[0]) , child = "Link" + str(i) , type = "revolute", position = self.directions[i], jointAxis = self.jointAxis[(j[0], i)])
                        break
        pyrosim.End()
        
