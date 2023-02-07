Nicket Mauskar Assignment 5

    Summary: 
        The goal of this project was to create a car-like robot that could carry a passenger(a cube) and carry it straight through 
        a pathway signified by obstacles without letting the cube fall. 

    Reproduction Steps: 
        1. run 'python search.py'
        2. once the 20 generations complete, 2 windows will pop up one over the other. One of them will be the worst possible 
        generation(the parent with the lowest fitness score), and the other will be the best possible generation(the parent with the
        highest score)
            Note: Sometimes during the generations, the program errors out and has a 'ValueError: could not convert string to float: '''. 
            It happens at completely random times and I still have not figured out how to prevent this from happening. If this happens, 
            close out of the program, and run the command from step 1 again. If it continues to happen, go to constants.py and reduce the 
            generations to 5 to ensure that it goes to completion!
    
    What I did: 
        1. Morphology 
            Changed the morphology of the robot from the quadraped to signify a car. I chose to put the spheres on the front of the car and 
            not on the back wheels because it produced better results as the spheres have less friction so the car was able to move forward 
            easier. I kept the square wheels underneath the spheres at approximately the same size so that the spheres touch the ground, but 
            are still in movement because the square wheels underneath provide some movement on the spheres as well. 
        2. Fitness Score
            The fitness score was based on 3 different aspects. It started off by declaring the score at 0, with the main goal being to get the
            highest fitness score.  
                1. y-Position: One of the goals of my project was to make sure the car travel  as far away from 
                the origin as possible in the y direction. The y-position was then added to the fitness score. 
                2. x-Position: Since I wanted the car to travel in a straight line and not just far away, I included a 10 point deduction to the 
                fitness score if it strayed out of the bounds of the straight pathway(x < -2, x > 3). If the x value was between -2 and 3, then 
                the fitness score remains the same. 
                3. ball height: I needed the car to maintain control of the ball height throughout its travels. In order to do this, I tracked the
                ball position throughout the cycle and if the position ever went below .4(aka the passenger/cube fell off the top of the car), There 
                would be a 50 point deduction to the fitness score. If the ball stayed on, the fitness score would remain the same. 
        3. Fitness function 
            As I explained before, the higher the fitness score, the better performance of the robot. As such, my fitness function was quite simple
            in that if the child fitness was greater than the parents fitness, then the parent would be the child, and so on. 
        
     

    

    
