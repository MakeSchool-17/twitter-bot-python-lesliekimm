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

    for i in range(0, last_index):
        # loop through words and delete punctuation
        current_word = list_of_all[i]
        print('WORD', current_word)

        # if last char of current_word is not a letter, remove char
        if current_word.isalpha() is False:
            print('CURRENT WORD', current_word)
            # check first char & remove if non letter
            if current_word[:1].isalpha() is False:
                current_word = current_word[1:]
                print(current_word)
            elif current_word[:-1].isalpha() is False:
                current_word = current_word[:-1]
                print(current_word)
            else:
                print(current_word)
                continue
            # check last char & remove if non letter
            # current_word = current_word[:-1]

        # if current_word is at least one char, convert all letters to
        # lower case and add to filtered_words
        if len(current_word) > 0:
            filtered_words.append(current_word)
    return filtered_words


def histogram(source_text):
    read_file = source_text.read()
    all_words = read_file.split(' ')

    histogram = []
    found_match = False

    histogram.append([all_words[0], 1])

    for i in range(1, len(all_words)):
        current_word = all_words[i]
        for j in range(0, len(histogram)):
            word_to_compare = histogram[j][0]
            if current_word == word_to_compare:
                histogram[j][1] += 1
                found_match = True
        if found_match is False:
            histogram.append([current_word, 1])
        else:
            i += 1

    print(histogram)
    return


def unique_words():
    return


def frequency():
    return

histogram(source_text)
