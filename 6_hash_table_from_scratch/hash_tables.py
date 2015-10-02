# class Node create instances of objects with key, value and next variables
class Node:
    # instantiates a Node ojbect with default values of None for key, value
    # and next members
    def __init__(self, key=None, value=None, next=None):
        self.key = key                  # word
        self.value = value              # frequency
        self.next = None

    # set the value of a Node object's member value
    def set_value(self, value):
        self.value = value
        return

    # return a Node object's value member
    def return_value(self):
        return self.value

    # print Node with value first formatted to right align of 10 chars
    # followed by the key
    def print_node(self):
        print('%10s' % self.value, '  ', self.key)
        return


# class Linked Lisk create instances of Linked Lists of Node objects with
# head and size variables.
class LinkedList:
    # instantiates a LinkedList object with default value of None for head
    # and size 0
    def __init__(self, head=None, size=0):
        self.head = None        # reference to first Node in LinkedList
        self.size = 0           # number of Nodes in LinkedList

    # inserts a Node object at the head of the LinkedList with key and value
    # members of Node set to parameters passed in
    def insert(self, key, value):
        # create a reference to the head
        temp = self.head
        # create new Node object
        new_node = Node(key, value)

        # if the current LinkedList is empty, set head to new_node
        if self.is_empty():
            self.head = new_node
        # if current LinkedList is not empty, insert node at the beginning
        # of LinkedList
        else:
            new_node.next = temp
            self.head = new_node
        # increment size of LinkedList
        self.size += 1
        return

    # searches LinkedList for key value passed in as paraemter and returns
    # a pointer to the corresponding Node
    def search(self, key):
        # create a reference to the head
        temp = self.head

        # if LinkedList is empty, print error message and return None
        if self.is_empty():
            print('ERROR: In LINKEDLIST class: There is nothing in this list.')
            return None
        # if LinkedList is not empty, search for key and return reference
        else:
            # traverse through list
            while temp is not None:
                # when key is found, return the reference to the Node object
                if temp.key is key:
                    return temp
                # if key does not match, set temp to next Node
                else:
                    temp = temp.next
            # if key was not found in LinkedList, print error message
            if temp is None:
                print('ERROR: In LINKEDLIST class: ' + key + ' not found. ' +
                      'Nothing to find.')
        return None

    # search for key passed in as parameter and assign new_value
    def update_value(self, key, new_value):
        # if LinkedList is empty, print error message
        if self.is_empty():
            print('ERROR: In LINKEDLIST class: There is nothing in this list.')
            return
        # if LinkedList is not empty, search for the key and update the value
        else:
            # search for key and create reference to the Node
            reference = self.search(key)
            # if key was found, set the Node's value to the new_value
            if reference is not None:
                reference.set_value(new_value)
            # if key is not found, print error message
            else:
                print('ERROR: In LINKEDLIST class: ' + key + ' not found. ' +
                      'Nothing to update.')
        return

    # returns True if LinkedList is empty and False if not empty
    def is_empty(self):
        return self.head is None

    # print the LinkedList
    def print_list(self):
        # create a reference to the head
        temp = self.head

        # if LinkedList is emmpty, print warning
        if self.is_empty():
            print('WARNING: In LINKEDLIST class. Nothing to print.')
        # if LinkedList is not empty, traverse through list and print node
        else:
            while temp is not None:
                temp.print_node()
                temp = temp.next
        return


class HashTable:
    def __init__(self, size=None):
        self.buckets_list = []
        self.keys = []
        self.values = []
        self.size = size

        for i in range(0, size):
            self.buckets_list.append(LinkedList())

    def insert(self, key, value):
        hashed_key = hash(key) % self.size
        self.buckets_list[hashed_key].insert(key, value)
        return

    def update_value(self, key, new_value):
        hashed_key = hash(key) % self.size
        linked_list_to_update = self.buckets_list[hashed_key]
        if linked_list_to_update.head is None:
            print('WARNING: In HASHTABLE class: Key not found. Nothing ' +
                  'to update.')
        else:
            node_to_update = linked_list_to_update.search(key)
            node_to_update.set_value(new_value)


if __name__ == '__main__':
    def test_node():
        # test Node class
        print('Testing Node class:')
        head = Node('head', 10)
        arm = Node('arm', 2)
        leg = Node('leg', 21)

        head.print_node()
        arm.print_node()
        leg.print_node()

        head.set_value(7)
        arm.set_value(3)
        leg.set_value(13)

        print('Updated Nodes:')
        head.print_node()
        arm.print_node()
        leg.print_node()

        print('Testing return_value function:')
        print('head', head.return_value())
        print('arm', arm.return_value())
        print('leg', leg.return_value())
        return

    def test_linked_list():
        # test LinkedList class
        print('Testing LinkedList class:')
        body = LinkedList()

        print('Testing is_empty function:')
        if body.is_empty():
            print('is_empty() works!')          # should print

        print('Testing print_list function for empty LinkedList:')
        body.print_list()                       # should print error message

        body.insert('head', 14)
        body.insert('arm', 6)
        body.insert('leg', 2)

        print('Testing insert and print_list function:')
        body.print_list()                       # should print 2, 6 14

        print('Testing search function:')
        reference_pointer1 = body.search('head')
        reference_pointer2 = body.search('leg')
        reference_pointer1.set_value(1)
        reference_pointer2.set_value(12)
        body.print_list()                       # should print 12, 6, 1

        print('Testing search function for key not in LinkedList:')
        reference_pointer3 = body.search('chest')       # should print error

        print('Testing update_value function:')
        body.update_value('leg', 20)
        body.update_value('head', 33)
        body.print_list()                       # should print 20, 6, 33

        print('Testing update_value function for key not in LinkedList:')
        body.update_value('thigh', 2)           # should print error
        return

    def test_hash_tables():
        return

    # test_node()
    test_linked_list()
