import sys
import re
# import random


SOURCE_TEXT = open('the_hobbit.txt')

# if the name of a text file is passed in as command line argument, set
# SOURCE_TEXT to argument
if len(sys.argv) > 1:
    SOURCE_TEXT = open(sys.argv[1])


# take an opened file as an argument and read the content, split the words
# and strip appropriate punctuation
def tokenization(source_text):
    read_file = source_text.read()
    words = re.split('\s|[!?.,;()"_:]+|', read_file)

    tokens = []

    for i in range(0, len(words)):
        current_word = words[i]
        if len(current_word) < 1:
            continue
        else:
            tokens.append(current_word)

    return tokens

if __name__ == '__main__':
    tokens = tokenization(SOURCE_TEXT)

    for i in range(0, len(tokens)):
        print(tokens[i])
