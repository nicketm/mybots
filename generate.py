import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0 
y = 0
z = .5
x1 = 0
y1 = 1
z1 = 1
for k in range(0, 4): 
    x = k
    y = 0
    z = .5
    for j in range(1, 5): 
        z = .5
        y += 1
        length = 1
        width = 1
        height = 1
        for i in range(1, 10): 
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            z+= 1
            length = .9*length
            width = .9*width
            height = .9*height
#pyrosim.Send_Cube(name="Box2", pos=[x1,y1,z1] , size=[length,width,height])

pyrosim.End()