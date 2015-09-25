import sys
import string

# open text file passed through as CL arg
source_text = open(sys.argv[1])


def main():
    return


# function that will read in each word from the source_text and returns
# a list of strings - will strip any puntcuation attached to the end of
def read_in_file(source_text):
    read_file = source_text.read()
    list_of_all = read_file.split(' ')
    print('TYPE OF LIST', type(list_of_all))

    # check end of each word to make sure there's no punctuation included

    for i in range(1000, 1050):
        current_word = list_of_all[i]
        
        print(current_word)

    print()
    return


def histogram(source_text):
    return


def unique_words():
    return


def frequency():
    return

read_in_file(source_text)
