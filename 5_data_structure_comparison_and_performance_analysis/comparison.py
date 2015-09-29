import sys
import re

source_text = open(sys.argv[1])


# reads in each word from source_text & returns list of strings
# will strip any punctuation attached to words
def read_in_data(source_text):
    # read file and append each word to list_of_all
    read_file = source_text.read()
    # list_of_all = read_file.split(' ')
    # list_of_all = re.split('\s|(?<!\d)[,.]|[,.](?!\d)', read_file)
    list_of_all = re.split('\s|[?!.,;()"_:]+', read_file)

    # initialize empty array for stripped words
    filtered_words = []

    # iterate through list_of_all and strip punctuation where
    # needed. append stripped words to filtered_words
    for i in range(0, len(list_of_all)):
        # get word of current index and convert to lower case
        current_word = list_of_all[i].lower()

        if len(current_word) == 0:
            continue
        else:
            # if the entire word is not alphabetic, strip word of
            # punctuation and append to filtered_words
            if current_word.isalpha() is False:
                # if first char of word is not alphabetic, remove first
                # char and append to filterd_words
                if current_word[0].isalpha() is False:
                    filtered_words.append(current_word[1:])
                # if last char of word is not alphabetic, remove last
                # char and append to filtered_words
                elif current_word[-1:].isalpha() is False:
                    filtered_words.append(current_word[:-1])
                # if punctuation was in the middle of word, leave as is
                else:
                    filtered_words.append(current_word)
                    # if there is no punctuation in word, append word as is
                    # to filtered_words
            else:
                filtered_words.append(current_word)

    return filtered_words

# get filtered_words_list
filtered_words_list = read_in_data(source_text)


# takes a source_text argument & return a histogram data struct that stores
# each unique word along w/ the # of times the word appears as a tuple
def histogram_tuple(source_text):
    # get filtered_words_list
    list_to_use = filtered_words_list
    # get length of list
    length_of_list = len(list_to_use)
    # initialize empty array
    tuple_histogram = []

    # iterate through the rest of filtered_words_list and append if
    # word is not currently in out_histogram or increment frequency
    while length_of_list > 0:
        # get the first word curently in the list
        current_word = list_to_use[0]
        # set frequency of that word to 1
        frequency_of_word = 1

        # iterate through the rest of the list & increase frequency
        # for each word found
        for i in range(1, length_of_list):
            if current_word == list_to_use[i]:
                frequency_of_word += 1
        # iterate through list and remove the current_word
        for j in range(0, frequency_of_word):
            list_to_use.remove(current_word)

        # deprecate the length_of_list by the frequency_of_word
        length_of_list -= frequency_of_word

        # if the length of the current_word is greater than 0, append
        # a tuple of the word and frequency to tuple_histogram
        if len(current_word) > 0:
            tuple_histogram.append([current_word, frequency_of_word])

    return tuple_histogram


# takes a word and histogram arguments and returns the frequency count
def frequency_tuple(word, in_histogram):
    for i in range(0, len(in_histogram)):
        if word == in_histogram[i][0]:
            return in_histogram[i][1]
    return None


def histogram_dictionary(source_text):
    # get filtered_words_list
    list_to_use = filtered_words_list
    # get length of list
    length_of_list = len(list_to_use)
    # initialize empty array
    dictionary_histogram = {}

    # iterate through the rest of filtered_words_list and append if
    # word is not currently in out_histogram or increment frequency
    while length_of_list > 0:
        # get the first word curently in the list
        current_word = list_to_use[0]
        # set frequency of that word to 1
        frequency_of_word = 1

        # iterate through the rest of the list & increase frequency
        # for each word found
        for i in range(1, length_of_list):
            if current_word == list_to_use[i]:
                frequency_of_word += 1
        # iterate through list and remove the current_word
        for j in range(0, frequency_of_word):
            list_to_use.remove(current_word)

        # deprecate the length_of_list by the frequency_of_word
        length_of_list -= frequency_of_word

        # if the length of the current_word is greater than 0, append
        # a tuple of the word and frequency to tuple_histogram
        if len(current_word) > 0:
            dictionary_histogram[current_word] = frequency_of_word

    return dictionary_histogram


def frequency_dictionary(word, in_histogram):
    return None


def histogram_sorted(source_text):
    sorted_histogram = []

    return sorted_histogram


def frequency_sorted(word, in_histogram):
    return None

# tupleH = histogram_tuple(source_text)
dictionaryH = histogram_dictionary(source_text)
# print('HISTOGRAM TUPLE', tupleH)
# print('FREQUENCY OF HELLO', frequency_tuple('hello', tupleH))
# print('FREQUENCY OF BYE', frequency_tuple('bye', tupleH))
# print('FREQUENCY OF THIS', frequency_tuple('this', tupleH))
print('HISTOGRAM DICTIONARY', type(dictionaryH), dictionaryH)
