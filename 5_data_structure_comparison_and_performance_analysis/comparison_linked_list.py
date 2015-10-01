import sys
import re

source_text = open(sys.argv[1])


# create a Node class that will hold a word, the frequency of the word
# and a pointer to the next Node
class Node:
    # constructor
    def __init__(self, word=None, frequency=None, next=None):
        self.word = word
        self.frequency = frequency
        self.next = next


# created a singly LinkedList class
class LinkedList:
    # constructor
    def __init__(self):
        self.head = None
        self.size = 0

    # insert a Node at the correct index - should be in order by frequency
    # of the word and the ASCII value of the word if there are multiple
    # words with the same frequency
    def insert(self, word, frequency):
        new_node = Node(word, frequency)
        temp = self.head

        # if the list is empty, set head to new_node
        if self.head is None:
            self.head = new_node
        # if the new word's freqency is less than the head, insert at head
        elif new_node.frequency < temp.frequency:
            new_node.next = temp
            self.head = new_node
            # if the new word's freqency is equal to the head, insert at head
        elif new_node.frequency is temp.frequency:
            new_node.next = temp
            self.head = new_node
        # if frequencies are the same, put in alphabetical order
        else:
            temp2 = temp
            temp = temp.next
            while temp.next is not None:
                if new_node.frequency < temp.frequency:
                    temp2.next = new_node
                    new_node.next = temp
                    break
                temp = temp.next
                temp2 = temp2.next
            if new_node.frequency <= temp.frequency:
                temp2.next = new_node
                new_node.next = temp
            else:
                temp.next = new_node

        # increment the size of the list
        self.size += 1
        return

    # print the list, frequency followed by the word
    def print_list(self):
        temp = self.head
        while temp is not None:
            print('%10s' % temp.frequency, '  ', temp.word)
            temp = temp.next
        return

    # return frequency of a word
    def frequency(self, word):
        temp = self.head
        thing_to_return = 0

        while temp is not None:
            print(temp.word, word, temp)
            if temp.word is word:
                thing_to_return = temp.frequency
                break
            else:
                temp = temp.next

        return thing_to_return


# takes a source_text argument & return a histogram data struct that stores
# each unique word along w/ the # of times the word appears as a tuple
def main(source_text):
    # get filtered_words_list
    list_to_use = read_in_data(source_text)
    # get length of list
    length_of_list = len(list_to_use)
    # initialize empty array
    ordered_linked_list = LinkedList()

    # iterate through the rest of list_to_use and append if
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
            ordered_linked_list.insert(current_word, frequency_of_word)

    ordered_linked_list.print_list()
    print('size of list', ordered_linked_list.size)
    print('frequency hello', ordered_linked_list.frequency('this'))
    return


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

main(source_text)
