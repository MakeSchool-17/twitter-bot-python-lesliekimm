import re

# read in dictionary file
i_file = open('/usr/share/dict/words', 'r')
read_in_file = i_file.read()
# remove all newline chars and put words into array
list_of_all = re.split('\n', read_in_file)


class AutocompleteWord:
    def __init__(self):
        self.partial_word = None
        self.list_of_words = []

    # iterate through list of all words and append words that start with
    # input string
    def get_list_of_words(self):
        for i in range(0, len(list_of_all)):
            if list_of_all[i].startswith(self.partial_word):
                self.list_of_words.append(list_of_all[i])

        return self.list_of_words


if __name__ == '__main__':
    # create a new AutocompleteWord object
    my_word = AutocompleteWord()
    # get input from user
    my_word.partial_word = input('Type the beginning of a word: ')
    # get list of words that match from dictionary
    words = my_word.get_list_of_words()
    print(words)
