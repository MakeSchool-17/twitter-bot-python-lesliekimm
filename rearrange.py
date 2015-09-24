# sys will allow access to command line arguments
# random will allow for shuffling
import sys
import random

# read in all command line arguments except file name
cl_args = sys.argv[1:]
# shuffle command line arguments
random.shuffle(cl_args)

# iterate through command line arguments and print
# separated by spaces
for i in cl_args:
    print(i, end=" ")

# print an extra line
print()
