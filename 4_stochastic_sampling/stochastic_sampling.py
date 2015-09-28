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
            out_histogram.append([filtered_words_list[i], 1])

    # for diagnostics
    print('NUM OF UNIQUE WORDS:', len(out_histogram))
    return out_histogram


# takes a histogram and returns any word at random - does not take probability
# into account
def randomWord(in_histogram):
    last_index = len(in_histogram) - 1
    random_index = random.randint(0, last_index)

    word_to_return = in_histogram[random_index][0]

    return word_to_return


# prove randomness of randomWord function for small body of text
def proveRandom(in_histogram):
    occurance_list = [[randomWord(in_histogram), 1]]
    new_word = True

    for i in range(0, 9999):
        new_random_word = randomWord(in_histogram)
        for j in range(0, len(occurance_list)):
            if new_random_word == occurance_list[j][0]:
                occurance_list[j][1] += 1
                new_word = False
                break
            else:
                new_word = True
        if new_word is True:
            occurance_list.append([new_random_word, 1])

    return occurance_list

generated_histogram = histogram(source_text)
print('RANDOM WORD:', randomWord(generated_histogram))
num_of_unique_words = len(generated_histogram)
print(num_of_unique_words)

occurance_histogram = proveRandom(generated_histogram)
print('PROVE RANDOM:')
print('EACH WORD HAS ~', 1/num_of_unique_words * 100, '% CHANCE')
for i in range(0, len(occurance_histogram)):
    percentage = (occurance_histogram[i][1]/10000) * 100
    print(occurance_histogram[i][0], ":", round(percentage, 2), "%")
# print('PROVE RANDOM:', proveRandom(generated_histogram))
