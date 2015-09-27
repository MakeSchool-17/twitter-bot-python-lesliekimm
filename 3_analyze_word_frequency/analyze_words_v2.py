import sys

# open text file passed through as CL arg
source_text = open(sys.argv[1])


# reads in each word from source_text & returns list of strings
# will strip any punctuation attached to words
def read_in_data(source_text):
    # read file and append each word to list_of_all
    read_file = source_text.read()
    list_of_all = read_file.split(' ')

    # initialize empty array for stripped words
    filtered_words = []

    # iterate through list_of_all and strip punctuation where
    # needed. append stripped words to filtered_words
    for i in range(0, len(list_of_all)):
        current_word = list_of_all[i]

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


# strips word of unnecessary punctuation and returns stripped_word
def strip_punctuation(word):
    stripped_word = 'BLANK'
    return stripped_word


# takes a source_text argument & returns a histogram data struct that
# stores each unique word along w/ the # of times the word appears
def histogram(source_text):
    filtered_words_list = read_in_data(source_text)

    print('IN HISTOGRAM')
    for i in range(0, len(filtered_words_list)):
        print(filtered_words_list[i])

    return out_histogram


def unique_words(in_histogram):
    return


def frequency(word, in_histogram):
    return

histogram(source_text)
