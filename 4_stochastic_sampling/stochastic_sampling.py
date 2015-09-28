import sys
import re
import random

# open text file passed through as CL arg
source_text = open(sys.argv[1])


# reads in each word from source_text & returns list of strings
# will strip any punctuation attached to words
def read_in_data(source_text):
    # read file and append each word to list_of_all
    read_file = source_text.read()
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


# takes a source_text argument & returns a histogram data struct that
# stores each unique word along w/ the # of times the word appears
def histogram(source_text):
    # get filtered_words_list
    filtered_words_list = read_in_data(source_text)
    # add first word to out_histogram with a frequency of 1
    out_histogram = [[filtered_words_list[0], 1]]
    # Boolean to indicate if word exists in out_histogram
    new_word = True

    # iterate through the rest of filtered_words_list and append if
    # word is not currently in out_histogram or increment frequency
    for i in range(1, len(filtered_words_list)):
        # iterate through out_histogram list
        for j in range(0, len(out_histogram)):
            # if the current word is the same as the current word in
            # out_histogram, increment frequency by 1
            if filtered_words_list[i] == out_histogram[j][0]:
                out_histogram[j][1] += 1
                new_word = False
                break
            # else, it is a new word
            else:
                new_word = True
        # if it is a new word, append the word w/ a frequency of 1
        if new_word is True:
            if len(filtered_words_list[i]) > 0:
                out_histogram.append([filtered_words_list[i], 1])

    return out_histogram


# takes a histogram and returns the total count of unique words
def unique_words(in_histogram):
    return len(in_histogram)


# takes a word and histogram and returns number of times that word
# appears in a text
def frequency(word, in_histogram):
    frequency_of_word = 0

    for i in range(0, len(in_histogram)):
        if word == in_histogram[i][0]:
            frequency_of_word = in_histogram[i][1]
    return frequency_of_word


# takes a histogram and returns any word at random - does not take probability
# into account
def random_word(in_histogram):
    # get the last index of the histogram
    last_index = len(in_histogram) - 1
    # generate a random number in the range of the length of the histogram
    random_index = random.randint(0, last_index)
    # get the word from the random selected index
    word_to_return = in_histogram[random_index][0]

    return word_to_return


# prove randomness of randomWord function for small body of text
def prove_random(in_histogram):
    # initialize new histogram that will keep track of number of times a
    # specific word is generated
    occurance_list = [[random_word(in_histogram), 1]]
    # Boolean used to keep track of whether a randomly generated word is
    # currently in the occurance_list histogram
    new_word = True

    # iterate through 10000 times (hardcoding in large sample size)
    for i in range(0, 9999):
        # generate a new random word
        new_random_word = random_word(in_histogram)
        # iterate through words in occurance_list
        for j in range(0, len(occurance_list)):
            # if the new word is in the list, increase the frequency by 1
            # and set new_word to False
            if new_random_word == occurance_list[j][0]:
                occurance_list[j][1] += 1
                new_word = False
                break
            # if the new word is not in th elist, set new_word to True
            else:
                new_word = True

        # if it is a new word, append it to the occurance_list histogram with
        # a frequency of 1
        if new_word is True:
            if len(new_random_word) > 0:
                occurance_list.append([new_random_word, 1])

    return occurance_list


def weighted_sampling(in_histogram):
    total_num_of_words = 0
    end_index = -1
    end_index_array = []

    for i in range(0, len(in_histogram)):
        total_num_of_words += in_histogram[i][1]

    for j in range(0, len(in_histogram)):
        end_index += in_histogram[j][1]
        end_index_array.append(end_index)

    random_weighted_index = random.randint(0, total_num_of_words - 1)

    for k in range(0, len(end_index_array)):
        if random_weighted_index <= end_index_array[k]:
            word_to_return = in_histogram[k][0]
            break

    return word_to_return

# diagnostics
# create histogram with sample text
generated_histogram = histogram(source_text)
# test random_word function
print('RANDOM WORD:', random_word(generated_histogram))
# get number of unique words & print
num_of_unique_words = unique_words(generated_histogram)
print(num_of_unique_words)

# run prove_random function
occurance_histogram = prove_random(generated_histogram)
print('PROVE RANDOM:')
uniform_percentage = 1/num_of_unique_words * 100
print('EACH WORD HAS ~', round(uniform_percentage, 2), '% CHANCE')
for i in range(0, len(occurance_histogram)):
    percentage = (occurance_histogram[i][1]/10000) * 100
    print(occurance_histogram[i][0], ":", round(percentage, 2), "%")

# run weighted_sampling function
print('WEIGHTED RANDOM WORD:', weighted_sampling(generated_histogram))
