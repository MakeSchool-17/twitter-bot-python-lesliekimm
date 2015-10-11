from heap import Heap
from tokenization import tokenize
from counting_tokens import HashTable
import sys


class HeapInterface():
    def __init__(self):
        # get a file to read words from user
        input_file = input('Please enter a file URL: ')

        SOURCE_TEXT = open(input_file)          # open file

        self.counts = Heap()                    # initialize Heap object
        tokens = tokenize(SOURCE_TEXT)          # create tokens from file
        hash_table = HashTable()                # create hash table

        # insert tokens into hash table
        for i in range(len(tokens)):
            hash_table.insert(tokens[i])

        # insert key value pairs into Heap
        for index in range(hash_table.num_of_buckets):
            if hash_table.buckets[index].is_empty():
                continue
            else:
                temp = hash_table.buckets[index].head
                while temp is not None:
                    pair = (temp.data[0], temp.data[1])
                    self.counts.insert(pair)
                    temp = temp.next

    def find_n_common_words(self, n):
        # DO THIS
        return

if __name__ == "__main__":
    interface = HeapInterface()
