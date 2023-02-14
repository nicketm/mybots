Nicket Mauskar Assignment 5

    Summary: 
        The goal of this project was to create a program that generates a kinematic chain (a jointed, motorized, innervated, sensorized snake) with a random number of randomly shaped links with random sensor placement along the chain.

    Reproduction Steps: 
        1. run 'python search.py'
    
    What I did: 
        1. Create random length snake with variable sizes: 
            I did this by specifying the length of the snake to be a random number between 2 and 10. Any higher number would work, but just for the purpose of this submission, I chose 2 and 10. Also, I made the sizes of the snake cubes to be a random number between .75 and 1.25 as to create difference in how they look 
            but still keep the functionality and appearance of a snake!
        2. Assigned neurons randomly and color coded accordingly. 
            I did this by creating a method in SOLUTION which takes the random number of total links(lets call this numlinks), and returns a list of a random length from 1...numlinks, in increasing order, of random numbers from 1...numlinks. I then 
            used this list as a guide to show which links will have sensor neurons and motor neurons connected to it. I also calibrated the send_cube function to assign the colors of the sensored links to green and the nonsensored links to blue. Lastly, 
            I made a method that basically chose a random joint axis to join the cubes out of x, y, and z axis. Any time i added a joint I called this method to randomize the axis of the joint to provide more variability. 
        
     

    

    
