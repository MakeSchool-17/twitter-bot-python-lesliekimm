import sys
import random

i_file = open('../../../../usr/share/dict/words', 'r')

num_of_words = int(sys.argv[1])
#print("NUM OF WORDS:", num_of_words) # printout statement
#print("FILE_TYPE", type(i_file))

read_in_file = i_file.readlines()
#print("READ_FILE_TYPE", type(read_in_file))

random_words = random.sample(read_in_file, num_of_words)
#print("RANDOM INDICIES:", random_words)

#for i in range(0, num_of_words):
#    print(random_words[i], end=" ")

for i in range(0, num_of_words):
    word_to_print = (random_words[i])[0:-1]
    print(word_to_print, end=" ")

print()
