import sys
import re


# hard code text file name to open
SOURCE_TEXT = open('the_hobbit.txt')

# if the name of a text file is passed in as command line argument, set
# SOURCE_TEXT to argument
if len(sys.argv) > 1:
    SOURCE_TEXT = open(sys.argv[1])


# take an opened file as an argument and read the content, split the words
# and strip appropriate punctuation
def tokenize(source_text):
    # read the source_text passed in
    read_file = source_text.read()
    # split words and strip punctuation
    words = re.split('\s|[!?.,;()"_:]+|', read_file)

    # initialize empty tokens array
    tokens = []

    # iterate through words array and add string from each index to tokens
    # array as long as it is not empty
    for index in range(0, len(words)):
        # get word of current indext
        current_word = words[index]

        # if current_word is empty, continue
        if len(current_word) < 1:
            continue
        # otherwise, add to tokens array
        else:
            tokens.append(current_word)

    return tokens

    # [brian] Instead of the above you could have written:

    for index, word in enumerate(words):
        if word:
            tokens.append(word)

    # Handling indices is something which comes up a lot and is very easy to
    # accidentally get wrong, so python goes out of its way to provide lots of
    # helpers that stop you from having to play with `index`. `enumerate` is
    # one of them and it's soooo nice

    return tokens


if __name__ == '__main__':
    tokens = tokenize(SOURCE_TEXT)

    # print all tokens
    for i in range(0, len(tokens)):
        print(tokens[i])

    # [brian] Instead of the above you could have written:
    for token in tokens:
        print(token)
