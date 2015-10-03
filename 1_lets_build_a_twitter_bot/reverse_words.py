import sys

# read in all command line arguments except file name
cl_args = sys.argv[1:]
# get the length of the list of args read in
length = len(cl_args)
# get the index of the last element
current_index = length - 1
# initialize a new array to put words
reversed_args = []

# append each word into reversed_args starting with the last word
while current_index >= 0:
    word = cl_args[current_index]
    reversed_args.append(word)
    current_index -= 1

# iterate through reversed_args array and print
for i in reversed_args:
    print(i, end=" ")

# print an extra line
print()
