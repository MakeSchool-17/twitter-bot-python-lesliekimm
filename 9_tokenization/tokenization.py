import sys
import re


# initialize source_text to open corpus.txt
source_text = open('the_hobbit.txt')
# if filename was passed through, open text file passed through as CL arg
if (len(sys.argv) > 1):
    source_text = open(sys.argv[1])


# reads in each word from source_text & returns list of strings
def parse_text(source_text):
    # read file and append each word to list_of_all
    read_file = source_text.read()
    list_of_all = re.split('\s+', read_file)

    # initialize empty array for stripped words
    filtered_words = []

    # iterate through list_of_all and keep punctuation/char case - this is in
    # order to keep track of words that are more likely to occur at the
    # beginning or end of sentence
    for i in range(0, len(list_of_all)):
        # get word of current index
        current_word = list_of_all[i]

        # if reading in an empty string, ignore and do not add to list
        if len(current_word) == 0:
            continue
        # otherwise, add current_word to list
        else:
            filtered_words.append(current_word)
    return filtered_words


if __name__ == "__main__":
    def test():
        returned_list = parse_text(source_text)
        for i in range(0, len(returned_list)):
            print(returned_list[i])
