import sys
import re

source_text = open(sys.argv[1])


class Node:
    def __init__(self, word=None, frequency=None, next=None):
        self.word = word
        self.frequency = frequency
        self.next = next

    def get_word(self):
        return self.word

    def get_frequency(self):
        return self.frequency

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head
