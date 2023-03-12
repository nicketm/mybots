from parallelHillClimber import PARALLEL_HILL_CLIMBER
from solution import SOLUTION
import os
import random 

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to continue...")
phc.Show_Best()
#phc.Show_Worst()


#for i in range(5): 
#   os.system("python3 generate.py")
#    os.system("python3 simulate.py")