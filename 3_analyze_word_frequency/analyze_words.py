import sys
import string

# open text file passed through as CL arg
source_text = open(sys.argv[1])


def main():
    return


# function that will read in each word from the source_text and returns
# a list of strings - will strip any punctuation attached to the end of
def read_in_file(source_text):
    # read file and append each word to list_of_all
    read_file = source_text.read()
    list_of_all = read_file.split(' ')

    # initialize empty array for stripped words
    filtered_words = []

    # get number of all words
    num_of_words = len(list_of_all)
    last_index = num_of_words - 1

    for i in range(0, 20):
        # loop through words and delete punctuation
        current_word = list_of_all[i]

        # if last char of current_word is not a letter, remove char
        if current_word.isalpha() is False:
            current_word = current_word[:-1]

        # if current_word is at least one char, convert all letters to
        # lower case and add to filtered_words
        if len(current_word) != 0:
            filtered_words.append(current_word.lower())
    return filtered_words


def histogram(source_text):
    filtered_words = read_in_file(source_text)
    for i in range(0, len(filtered_words)):
        print(filtered_words[i])

    return


def unique_words():
    return


def frequency():
    return

histogram(source_text)
