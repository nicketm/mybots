from parallelHillClimber import PARALLEL_HILL_CLIMBER
from solution import SOLUTION
import os

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
phc.Show_Worst()


#for i in range(5): 
#   os.system("python3 generate.py")
#    os.system("python3 simulate.py")