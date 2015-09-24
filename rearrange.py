import sys
import random

cl_args = sys.argv[1:]
random.shuffle(cl_args)

for i in cl_args:
    print(i, end=" ")

print()
