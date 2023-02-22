import numpy as np 
import pyrosim.pyrosim as pyrosim
import random
import os 
import time
import constants as c



class SOLUTION: 
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.numlinks = np.random.randint(7, 8) 
        print('numlinks', self.numlinks)
        self.numjoints = self.numlinks - 1
        self.weights = np.random.rand(self.numlinks, self.numjoints)
        self.weights = self.weights * 2 - 1
        self.sensor_ind = self.create_sensor_ind()
        self.numsensor = len(self.sensor_ind)
        #self.numlinks = 2 
        print('sensor ind', self.sensor_ind)
        self.joints = []


    def Start_Simulation(self, guiOrDirect): 
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        #os.system("python simulate.py " + guiOrDirect)
        os_string = ("python3 simulate.py " + guiOrDirect + " " + str(self.myID) + " &")

        os.system(os_string)
    def Wait_For_Simulation_To_End(self): 
        fitness_s = 'fitness' + str(self.myID) + '.txt'
        while not os.path.exists(fitness_s):
            time.sleep(0.01)
        f = open(fitness_s, "r")
        self.fitness = float(f.read())
        #print(self.fitness)
        f.close()
        os.system('rm '+fitness_s)

    def Create_World(self): 
        length = 1
        width = 1
        height = 1
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[0,0,0] , size=[20,4,.2])
        #pyrosim.Send_Cube(name="Box", pos=[-3,0,0] , size=[1,1,1])
        pyrosim.End()


    def Generate_Body(self): 
        self.joints = []
        sizex =  np.random.uniform(.2, 2)
        sizey =  np.random.uniform(.2, 2)
        sizez =  np.random.uniform(.2, 2)
        pyrosim.Start_URDF("body.urdf")
        directionx = {}
        collision = {}

        # start link
        pyrosim.Send_Cube(name="Link" + str(0), pos=[0,0,1.25] , size=[sizex, sizey, sizez], color = 'blue')
        JA = self.generate_joint_axis()
        #pyrosim.Send_Joint( name = "Link" + str(0) + "_Link" + str(1) , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1.25], jointAxis = JA)
        self.joints.append((0, 1))
        directionx[0] = [0, 0, 0, 'x']
        collision[0] = ['x']
        for i in range(1, self.numlinks): 
            sizex =  np.random.uniform(.75, 1.25)
            sizey =  np.random.uniform(.75, 1.25)
            sizez =  np.random.uniform(.75, 1.25)
            randkey = random.choice([k for k in directionx.keys()])
            xyz = np.random.randint(1, 4)

            if xyz == 1: # positive x
                #randkey = random.choice([k for k in directionx.keys()])
               # directionx[i] = self.create_direction(prevmax, sizex, 'x')
                #prevmax = directionx[randkey]
                colcheck = self.collision_checker(collision[randkey], 'x')
                self.check_collision(collision, randkey, 'x')
                self.check_collision(collision, i, 'z')
                #colcheck = self.collision_checker(collision[randkey], 'x')
                
                sb = False
                if colcheck is False: 
                    prevmax = directionx[randkey]
                    directionx[i] = self.create_direction(prevmax, sizex, 'x')
                    if i in self.sensor_ind: 
                        sb = True
                        pyrosim.Send_Cube(name="Link" + str(i), pos=[sizex, 0, 0] , size=[sizex, sizey, sizez], color = 'green')
                    else: 
                        pyrosim.Send_Cube(name="Link" + str(i), pos=[sizex, 0, 0] , size=[sizex, sizey, sizez], color = 'blue')
                    JA = self.generate_joint_axis()
                    pyrosim.Send_Joint( name = "Link" + str(randkey) + "_Link" + str(i) , parent= "Link" + str(randkey) , child = "Link" + str(i) , type = "revolute", position = directionx[i], jointAxis = JA)
                    self.joints.append((randkey, i))
                else: 
                    xyz += 1
            if xyz == 2: # positive z
                #randkey = random.choice([k for k in directionx.keys()])
               # prevmax = directionx[randkey]
              #  directionx[i] = self.create_direction(prevmax, sizez, 'z')
                colcheck = self.collision_checker(collision[randkey], 'z')
                self.check_collision(collision, randkey, 'z')
                self.check_collision(collision, i, 'z')
               # colcheck = self.collision_checker(collision[randkey], 'z')
                if colcheck is False: 
                    prevmax = directionx[randkey]
                    directionx[i] = self.create_direction(prevmax, sizez, 'z')
                    if i in self.sensor_ind: 
                        pyrosim.Send_Cube(name="Link" + str(i), pos=[0, sizey, 0] , size=[sizex, sizey, sizez], color = 'green')
                    else: 
                        pyrosim.Send_Cube(name="Link" + str(i), pos=[0, sizey, 0] , size=[sizex, sizey, sizez], color = 'blue') 
                    JA = self.generate_joint_axis()
                    pyrosim.Send_Joint( name = "Link" + str(randkey) + "_Link" + str(i) , parent= "Link" + str(randkey) , child = "Link" + str(i) , type = "revolute", position = directionx[i], jointAxis = JA) 
                    self.joints.append((randkey, i))
                else: 
                    xyz += 1
            if xyz == 3: # positive y
                #randkey = random.choice([k for k in directionx.keys()])
                #prevmax = directionx[randkey]
               # directionx[i] = self.create_direction(prevmax, sizey, 'y')
                colcheck = self.collision_checker(collision[randkey], 'y')
                self.check_collision(collision, randkey, 'y')
                #colcheck = self.collision_checker(collision[randkey], 'y')
                self.check_collision(collision, i, 'z')
                
                if colcheck is False:
                    prevmax = directionx[randkey] 
                    directionx[i] = self.create_direction(prevmax, sizey, 'y')
                    if i in self.sensor_ind: 
                        pyrosim.Send_Cube(name="Link" + str(i), pos=[0, 0, sizez] , size=[sizex, sizey, sizez], color = 'green')
                    else: 
                        pyrosim.Send_Cube(name="Link" + str(i), pos=[0, 0, sizez] , size=[sizex, sizey, sizez], color = 'blue')
                    JA = self.generate_joint_axis()
                    pyrosim.Send_Joint( name = "Link" + str(randkey) + "_Link" + str(i) , parent= "Link" + str(randkey) , child = "Link" + str(i) , type = "revolute", position = directionx[i], jointAxis = JA)
                    self.joints.append((randkey, i))
                else: 
                    xyz += 1
            if xyz == 4: # negative 
            #randkey = random.choice([k for k in directionx.keys()])
            # prevmax = directionx[randkey]
            #  directionx[i] = self.create_direction(prevmax, sizez, 'z')
                colcheck = self.collision_checker(collision[randkey], '-x')
                self.check_collision(collision, randkey, '-x')
                self.check_collision(collision, i, '-x')
                #colcheck = self.collision_checker(collision[randkey], '-x')
                #if colcheck is False: 
                prevmax = directionx[randkey]
                directionx[i] = self.create_direction(prevmax, sizez, '-x')
                if i in self.sensor_ind: 
                    pyrosim.Send_Cube(name="Link" + str(i), pos=[0, sizey, 0] , size=[sizex, sizey, sizez], color = 'green')
                else: 
                    pyrosim.Send_Cube(name="Link" + str(i), pos=[0, sizey, 0] , size=[sizex, sizey, sizez], color = 'blue') 
                JA = self.generate_joint_axis()
                pyrosim.Send_Joint( name = "Link" + str(randkey) + "_Link" + str(i) , parent= "Link" + str(randkey) , child = "Link" + str(i) , type = "revolute", position = directionx[i], jointAxis = JA) 
                self.joints.append((randkey, i))
                #else: 
                    #continue

        print(collision)
        pyrosim.End()


    def Generate_Brain(self): 
        print('IN GENERATE BRAIN')
        print('brain:   ', self.joints)
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
        sensorcnt = 0
        for i in range(len(self.sensor_ind)):
            pyrosim.Send_Sensor_Neuron(name = sensorcnt , linkName = "Link"+ str(self.sensor_ind[i]))
            sensorcnt += 1
        motorjointcount = 0
        for i in range((len(self.joints))): 
            if self.joints[i][0] in self.sensor_ind or self.joints[i][1] in self.sensor_ind: 
                motorjointcount += 1
                jointName1 = "Link" + str(self.joints[i][0]) + "_Link" + str(self.joints[i][1])
                pyrosim.Send_Motor_Neuron( name = sensorcnt , jointName = jointName1)
                sensorcnt += 1
        for currentRow in range(len(self.sensor_ind)): 
            for currentColumn in range(motorjointcount): 
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+ self.numsensor , weight = self.weights[currentRow][currentColumn] )
    

    



    def Mutate(self): 
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
    
    def Set_ID(self, id): 
        self.myID = id

    def create_sensor_ind(self): 
        length = np.random.randint(1, self.numlinks)
        lst = []
        for i in range(length): 
            lst.append(np.random.randint(2, self.numlinks))
        unqlst = list(set(lst))
        return unqlst
        
    def generate_joint_axis(self): 
        ind = np.random.randint(0, 3)
        lst = ["1 0 0", "0 1 0", "0 0 1"]
        return lst[ind]
    
    def create_direction(self, pos, size, dir): 
        if pos[3] == 'x': 
            #if dir == 'y': 
            #    return [size, pos[1] - size, pos[2], dir]
            #else: 
            return [size, pos[1], pos[2], dir]
        if pos[3] == 'z': 
            #if dir == 'z': 
            #    return [pos[0], pos[1], size, dir]
            #if dir == 'x': 
            #    return [pos[0] - size, pos[1], size, dir]
            #if dir == 'y': 
            return [pos[0], pos[1], size, dir]

        if pos[3] == 'y':
            #if dir == 'x':  
            #    return [pos[0] - size, size, pos[2], dir]
            #else: 
            return [pos[0], size, pos[2], dir] 
        if pos[3] == '-x':
            #if dir == 'x':  
            #    return [pos[0] - size, size, pos[2], dir]
            #else: 
            return [-1 * size, pos[1], pos[2], dir] 
        if pos[3] == '-y':
            #if dir == 'x':  
            #    return [pos[0] - size, size, pos[2], dir]
            #else: 
            return [pos[0], -1*size, pos[2], dir] 
    def check_collision(self, dict, key, dir):
        if key in dict.keys(): 
            if dir not in dict[key]: 
                dict[key].append(dir)
        else: 
            dict[key] = [dir] 
    
    def collision_checker(self, vector, dir): 
        print(vector)
        print(dir)
        for i in vector: 
            if dir == i: 
                return True
        return False

        
        


