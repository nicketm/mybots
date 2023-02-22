Nicket Mauskar Assignment 7

    Summary: 
        The goal of this project was to create a random 3-d morphology that is contihious, able in principle to fill 3d space, and obey the laws of physics. 

    Reproduction Steps: 
        1. run 'python search.py'
    
    What I did: 
        1. Create randomly sized creature with variable sizes: 
            I did this by specifying the length/size of the creature to be a random number between 5 and 15. Any higher number would work, but just for the purpose of this submission, I chose 5 and 15. Also, I made the sizes of the cubes to be a random number between .2 and 2 to create some variability.
        2. Assigned neurons randomly and color coded accordingly. 
            I did this by creating a method in SOLUTION which takes the random number of total links(lets call this numlinks), and returns a list of a random length from 1...numlinks, in increasing order, of random numbers from 1...numlinks. I then used this list as a guide to show which links will have sensor neurons and motor neurons connected to it. I also calibrated the send_cube function to assign the colors of the sensored links to green and the nonsensored links to blue. Lastly, I made a method that basically chose a random joint axis to join the cubes out of x, y, and z axis. Any time i added a joint I called this method to randomize the axis of the joint to provide more variability. 
        3. Generate a random direction and attach the link to a randomly chosen previous link with a collision check. 
            Generated a random number 1-5 which signified the directions of expansion(+x, +y, +z, -x, -y). After this, it randomly chooses a link from a dictionary of already established links (every time I add a link, I add the linkname: position into a dictionary). I also have a collision checker dictionary which keeps track of all the directions that a certain link has expanded to, and before adding another link, I check if the cube has been expanded in the randomly chosen direction already. If it has, then I choose another direction and try again. If not, then I continue to expand the creature with less chances of collisions. 
        4.  Constantly Update the links dictionary and collision dictionary
            Everytime a new link is placed, I make sure to update these two dictionaries such that any time I add a new link to a random link from before, I have all the position, joint, and axis information of that parent link such that my child link will have the most optimal position and connection with said parent link. 

    Diagram: *** PLEASE REFER TO DIAGRAMREADME.jpg to see a visual diagram on how the first 3...n cubes would be generated. ***


        
     

    

    
