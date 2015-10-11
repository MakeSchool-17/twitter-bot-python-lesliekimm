import sys
import re
import random

# hard code text file name to open and number of words to make random senence
SOURCE_TEXT = open('test.txt')
NUM_OF_WORDS = 10

# if the name of a text file is passed in as command line argument, set
# SOURCE_TEXT to argument
if len(sys.argv) > 1:
    SOURCE_TEXT = open(sys.argv[1])


# take an opened file as an argument and read the content, split the words
# and strip appropriate punctuation
def tokenize(source_text):
    # read the source_text passed in
    read_file = source_text.read()
    # split words and strip punctuation
    words = re.split('\s|[!?.,;()"_:]+|', read_file)

    # initialize empty tokens array
    tokens = []

    # iterate through words array and add string from each index to tokens
    # array as long as it is not empty
    for index in range(0, len(words)):
        # get word of current indext
        current_word = words[index]

        # if current_word is empty, continue
        if len(current_word) < 1:
            continue
        # otherwise, add to tokens array
        else:
            tokens.append(current_word)

    return tokens


# Node class creates objects with data and next variables
class Node:
    # creates Node object with data and next parameters passed in
    # data is a list of string key and int value - ['key', value]
    def __init__(self, data=None, next=None):
        self.data = data                    # iniitalize data
        self.next = next                    # initialize next

    # return formatted output method to return data[1] (value) align right in
    # 10 spaces followed by the data[0] (key)
    def __str__(self):
        str_to_return = '%10s' % self.data[1] + '  ' + self.data[0]
        return str_to_return


# LinkedList class creates objects with head and size variables
class LinkedList:
    # creates empty LinkedList object with head set to None and size to zero
    def __init__(self):
        self.head = None                    # initialize to None for empty LL
        self.size = 0                       # initalize to zero Nodes in LL

    # return True if a new Node was inserted for key passed in and False if
    # no new Node was created
    def insert(self, key, value=None):
        # if empty LL, insert new Node at head and increment size
        if self.head is None:
            # if value is not passed in
            if value is None:
                self.head = Node([key, 1], None)
            # if refactoring, use value in inserting new Node
            else:
                self.head = Node([key, value], None)
            self.size += 1
        # it not empty LL
        else:
            # create a reference to head of LL
            temp = self.head

            # while the next node is not None
            while temp.next is not None:
                # if the key is equal to the temp Node;s key, increment temp
                # Node's value and return False
                if key == temp.data[0]:
                    temp.data[1] += 1
                    return False
                # if key does not equal temp Node's key, set temp to next Node
                else:
                    temp = temp.next

            # temp is at last Node in list - if key is equal to last Node's,
            # key, increment temp Node's value and return False
            if key == temp.data[0]:
                temp.data[1] += 1
                return False
            # otherwise, add new Node at end of LL and increment size
            else:
                temp.next = Node([key, 1], None)
                self.size += 1

        # return True when new Nodes are added
        return True

    # iterate through LL and print each Node
    def print_linked_list(self):
        # create a reference to head of LL
        temp = self.head

        # while temp is not None
        while temp is not None:
            # print each Node and set temp to next Node
            print(temp)
            temp = temp.next

        return

    # return True if LL is empty and False otherwise
    def is_empty(self):
        return self.size is 0


# HashTable class creates objects with buckets, numb of buckets, buckets used
# num of keys and load factor variables
class HashTable:
    # creates HashTable object with a buckets array of size 10000 each holding
    # a pointer to an empty LL and buckets_used, num_of_keys and load_factor
    # set to 0
    def __init__(self):
        self.buckets = []                   # initialize empty list of buckets
        self.num_of_buckets = 1000          # initialize 10000 buckets
        self.buckets_used = 0               # 0 buckets used
        self.num_of_keys = 0                # start with 0 keys
        self.load_factor = 0                # empty load factor
        self.refactor_x = 0                 # keep track of how many refactors
        self.current_end_index = 0          # keeps track of total tokens

        # create empty LinkedList for initial 10000 buckets
        for index in range(self.num_of_buckets):
            self.buckets.append(LinkedList())

    # hashes key passed in and inserts key into hashed_key index of the
    # buckets list - refactors whenever load_factor becomes greater than 66.67%
    def insert(self, key, value=None):
        # hash key and locate list_to_use
        hashed_key = hash(key) % self.num_of_buckets
        list_to_use = self.buckets[hashed_key]

        # if the HashTable is empty or if the list_to_use is empty, insert
        # key into HashtTable, increment num_of_keys and buckets_used and
        # calculate new load_factor
        if (self.num_of_keys == 0) or (list_to_use.is_empty() is True):
            # if not refactoring
            if value is None:
                new_key = list_to_use.insert(key)
            # if refactoring, use value as a parameter in inserting
            else:
                new_key = list_to_use.insert(key, value)
            self.num_of_keys += 1
            self.buckets_used += 1
            self.load_factor = self.buckets_used / self.num_of_buckets
        # otherwise, insert key into HashTable
        else:
            # insert new_key into HashTable
            new_key = list_to_use.insert(key)

            # if inserting new Node into LL, increment num_of_keys
            if new_key is True:
                self.num_of_keys += 1

        # if load_factor is greater than 66.67% and refactor
        if self.load_factor > 2/3:
            self.refactor()

        return

    def refactor(self):
        print('REFACTORING')
        # create a reference of all Nodes by storing them as [key, value] list
        temp_nodes = []

        # iterate through HashTable
        for index in range(self.num_of_buckets):
            # if the bucket is empty, continue
            if self.buckets[index].is_empty():
                continue
            # otherwise, traverse through list and append each [key, value]
            # pair to temp_nodes
            else:
                # creat a reference to LL head
                temp = self.buckets[index].head

                # while temp is not None
                while temp is not None:
                    # append each [key, value] and set temp to next
                    temp_nodes.append([temp.data[0], temp.data[1]])
                    temp = temp.next

        self.num_of_buckets *= 2            # double number of buckets
        del self.buckets[:]                 # clear self.buckets list
        self.buckets_used = 0               # reset buckets_used to 0
        self.num_of_keys = 0                # reset num_of_keys to 0
        self.load_factor = 0                # reset load_factor to 0
        self.refactor_x += 1                # increment refactor_x

        # initialize new buckets to point to empty LL
        for index in range(0, self.num_of_buckets):
            self.buckets.append(LinkedList())

        # insert previously stored keys into HashTable with current value
        for index in range(len(temp_nodes)):
            self.insert(temp_nodes[index][0], temp_nodes[index][1])

        return

    # returns a frequency distribution by inserting lists of [key, end index]
    def return_distribution(self):
        distribution = []                   # initialize empty list

        # iterate through all buckets in HashTable
        for index in range(self.num_of_buckets):
            # if bucket is empty, skip
            if self.buckets[index].is_empty():
                continue
            # otherwise, create a reference to it's LL head and calculate
            # the end index which will represent it's distribution
            else:
                # create a reference to head
                temp = self.buckets[index].head

                # while temp is not None
                while temp is not None:
                    self.current_end_index += temp.data[1]
                    frequency = [temp.data[0], self.current_end_index]
                    distribution.append(frequency)
                    temp = temp.next

        return distribution

    # returns a random word selected from the distribution
    def select_random_word(self, distribution):
        random_word = ''                    # initialize to empty string
        # pick a random index from 0 to current_end_index
        random_index = random.randint(0, self.current_end_index - 1)
        print('end index:', self.current_end_index)
        print(random_index)

        # iterate through distribution and if the random_index is less than
        # the index's current_end_index, return the index's key and break
        for index in range(len(distribution)):
            if random_index < distribution[index][1]:
                random_word = distribution[index][0]
                print('random word: ', random_word)
                break

        return random_word

    # prints the bucket number followed by each key, value pair
    def print_hash_table(self):
        # iterate through buckets
        for index in range(self.num_of_buckets):
            # if bucket is empty, skip
            if self.buckets[index].is_empty():
                continue
            # otherwise, print bucket number and print it's LL
            else:
                print('Bucket: ', index)
                self.buckets[index].print_linked_list()

        return


def generate_sentence(num_of_words, hash_table):
    sentence = ''
    hash_table.current_end_index = 0
    distribution = hash_table.return_distribution()

    for i in range(num_of_words):
        word_to_add = hash_table.select_random_word(distribution)
        sentence += word_to_add + ' '

    return sentence

if __name__ == "__main__":
    tokens = tokenize(SOURCE_TEXT)

    def testHobbitHT():
        HT = HashTable()
        for i in range(len(tokens)):
            HT.insert(tokens[i])

        HT.print_hash_table()
        print('NUM OF KEYS: ', HT.num_of_keys)
        print('BUCKETS USED: ', HT.buckets_used)
        print('LOAD FACTOR: ', HT.load_factor)
        print('REFACTORED: ', HT.refactor_x)

        hist = HT.return_distribution()
        print(hist)
        word = HT.select_random_word(hist)
        print(word)
        word = HT.select_random_word(hist)
        print(word)
        word = HT.select_random_word(hist)
        print(word)
        word = HT.select_random_word(hist)
        print(word)
        word = HT.select_random_word(hist)
        print(word)

        print(generate_sentence(35, HT))

    def testHT():
        HT = HashTable()
        HT.insert('blue')
        HT.insert('green')
        HT.insert('blue')
        HT.insert('yellow')
        HT.insert('green')
        HT.insert('green')
        HT.insert('green')
        HT.insert('green')
        HT.insert('brown')
        HT.print_hash_table()
        print('NUM OF KEYS: ', HT.num_of_keys)
        print('BUCKETS USED: ', HT.buckets_used)
        print('LOAD FACTOR: ', HT.load_factor)

    def testLL():
        LL = LinkedList()
        print(LL.is_empty())
        LL.insert('orange')
        LL.insert('blue')
        LL.insert('yellow')
        LL.insert('red')
        LL.insert('blue')
        LL.insert('black')
        LL.insert('orange')
        LL.insert('orange')
        LL.insert('brown')
        LL.insert('brown')
        print(LL.size)
        print(LL.is_empty())

        temp = LL.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    #testLL()
    testHobbitHT()
