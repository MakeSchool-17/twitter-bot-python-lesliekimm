# sys will allow access to command line arguments
# random will allow to sample words from file
import sys
import random

# read in number of words to randomly select
num_of_words = int(sys.argv[1])
# hardcoded directory URL for dictionary file, open as read only
i_file = open('/usr/share/dict/words', 'r')

# read in each line of the file
read_in_file = i_file.readlines()
# sample num_of_words words from read in file
random_words = random.sample(read_in_file, num_of_words)

# iterate through random_words list and print separated by spaces
for i in range(0, num_of_words):
    # last character of each line read in is a newline so do not
    # read in last character
    word_to_print = (random_words[i])[0:-1]
    print(word_to_print, end=" ")

# print an extra line
print()
