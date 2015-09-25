# sys will allow access to command line arguments
# random will allow for shuffling
import sys

# read in all command line arguments except file name
cl_args = sys.argv[1:]
length = len(cl_args)
current_index = length - 1
reversed_args = []

# append each word into reversed_args starting with the
# last word
while current_index >= 0:
    word = cl_args[current_index]
    reversed_args.append(word)
    current_index -= 1

# iterate through reversed_args array and print
for i in reversed_args:
    print(i, end=" ")

# print an extra line
print()
