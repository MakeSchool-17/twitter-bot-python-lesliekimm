# [brian] All the newlines in this file are awesome, they make it a LOT
# easier to read.

# class Node create instances of objects with key, value and next variables
class Node:
    # instantiates a Node ojbect with default values of None for key, value
    # and next members
    def __init__(self, key=None, value=None, next=None):
        self.key = key                  # word
        self.value = value              # frequency
        self.next = None                # pointer to next Node

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


# class Linked Lisk create instances of lists of Node objects with
# head and size variables.
class LinkedList:
    # instantiates a LinkedList object with default value of None for head
    # and size 0
    def __init__(self, head=None, size=0):
        self.head = None                # reference to first Node in LinkedList
        self.tail = None                # reference to last Node in LinkedList
        self.size = 0                   # number of Nodes in LinkedList

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
            self.tail = new_node
        # if current LinkedList is not empty, insert node at the beginning
        # of LinkedList
        else:
            new_node.next = temp
            self.head = new_node
        # increment size of LinkedList
        self.size += 1
        return

    # search for key in LinkedList and remove the corresponding Node
    def delete(self, key):
        # create a reference to the head
        temp = self.head

        # if LinkedList is empty, print error message and return None
        if self.is_empty():
            print('ERROR: In LINKEDLIST class: There is nothing in this list.')
            return
        # if LinkedList is not empty, delete Node and update size
        else:
            # if the first Node contains key, update head and decrement size
            if temp.key is key:
                self.head = self.head.next
                self.size -= 1
                return
            # otherwise, traverse through LinkedList
            else:
                # create a trailing reference pointer
                temp2 = temp
                temp = temp.next
                # traverse through list
                while temp is not None:
                    # when found, update temp2 next variable and decrement size
                    if temp.key is key:
                        temp2.next = temp.next
                        self.size -= 1
                        return
                    # otherwise, set both temp and temp2 to the next variable
                    else:
                        temp2 = temp
                        temp = temp.next
                # if key was not found in LinkedList, print error message
                if temp is None:
                    print('ERROR: In LINKEDLIST class: ' + key + ' not ' +
                          'found. Nothing to delete.')
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

    # traverse through list and append key of each Node to list_of_keys and
    # return list_of_keys
    def return_keys(self):
        # create reference to the head
        temp = self.head
        # initialize an empty array
        list_of_keys = []

        # traverse through list and append key of each Node to list_of_keys
        while temp is not None:
            list_of_keys.append(temp.key)
            temp = temp.next

        return list_of_keys

    # traverse through list and append key of each Node to list_of_values and
    # return list_of_values
    def return_values(self):
        # create reference to the head
        temp = self.head
        # initialize an empty array
        list_of_values = []

        # traverse through list and append key of each Node to list_of_values
        while temp is not None:
            list_of_values.append(temp.value)
            temp = temp.next

        return list_of_values

# class HashTable creates lists of LinkedList objects with buckets_lists, keys
# values and size variables
class HashTable:
    # creates a HashTable that initializes empty LinkedLists for each index
    # in buckets_lists, empty lists for keys and values, sets size to
    # paramerter passed in, sets num_of_items to 0 and sets empty to True
    def __init__(self, size=0):
        self.buckets_list = []          # list of buckets of LinkedLists
        self.size = size                # number of pointers in buckets_list
        self.num_of_items = 0           # number of Nodes in entire HashTable
        self.empty = True               # indicates if HashTable is empty

        # initialize buckets_list to be length of size passed in and
        # initialize a LinkedList object for each index of buckets_list
        for i in range(0, size):
            self.buckets_list.append(LinkedList())

        # [brian] For the above you could write:

        self.buckets_list = [LinkedList() for _ in range(size)]

    # returns number of total key-value pairs entered
    def return_num_of_items(self):
        return self.num_of_items
    # [brian] Since you're already using `__getitem__` and `__setitem__`,
    # you could implement `__len__` instead of `return_number_of_items`,
    # that would let you call `len(hash_table)`.

    # insert key and value into correct bucket after hashing key, update
    # key and values list to include new key and value, increment size
    def insert(self, key, value):
        # calculate hashed_key and determine which bucket key-value pair
        # will go into
        hashed_key = hash(key) % self.size
        # insert into appropriate index
        self.buckets_list[hashed_key].insert(key, value)
        # add key to list of all keys
        self.num_of_items += 1
        # set empty variable to False
        self.empty = False
        return # [brian] You don't need this line, if you don't include a
               # return statement python will return automatically.

    def delete(self, key):
        # hash the key and find the correct LinkedList to search
        hashed_key = hash(key) % self.size
        list_to_search = self.buckets_list[hashed_key]

        # print error if list is empty
        if list_to_search.is_empty():
            print('ERROR: In HASHTABLE class: Searching incorrect list.')
            return
        # if LinkedList is not empty, traverse list and delete correct Node
        else:
            list_to_search.delete(key)
            self.num_of_items -= 1
            return

    # search for key in HashTable and return the value
    def get(self, key):
        # hash the key and find the correct LinkedList to search
        hashed_key = hash(key) % self.size
        list_to_search = self.buckets_list[hashed_key]

        # print error if list is empty
        if list_to_search.is_empty():
            print('ERROR: In HASHTABLE class: Searching incorrect list.')
            return None
        # if LinkedList is not empty, traverse list and return value for key
        else:
            # create a reference to LinkedList head
            temp = list_to_search.head

            # traverse through list until key is found
            while temp is not None:
                if temp.key is key:
                    return temp.value
                temp = temp.next
            # if key is not found, print an error message
            else:
                print('ERROR: In HASHTABLE class: ' + key + ' not found.')
                return None

    # update the value of the key passed in with the new_value and update
    # the values list
    def __setitem__(self, key, new_value):
        # [brian] Nice! Using things like __setitem__ makes your code
        # so much nicer and easier to read. magic methods let you take
        # advantage of the cool syntax I'm sure you're already missing
        # in the obj-c coding you're doing now.

        # hash the key and find the correct LinkedList to search
        hashed_key = hash(key) % self.size
        list_to_update = self.buckets_list[hashed_key]

        # print error if list is empty
        if list_to_update.is_empty():
            raise KeyError('In HASHTABLE class: Searching incorrect list.')
        # if LinkedList is not empty, search for key and replace value
        else:
            # create reference to Node with correct key
            ref_to_node = list_to_update.search(key)
            if ref_to_node is not None:
                # assign new value
                ref_to_node.value = new_value
            else:
                raise KeyError('In HASHTABLE class: Key does not exist.')

    # returns True if HashTable is empty and false otherwise
    def is_empty(self):
        return self.empty

    # print HashTable
    def print_hash_table(self):
        # if HashTable is empty, print warning
        if self.empty:
            print('WARNING: In HASHTABLE class: Hash Table is empty. ' +
                  'Nothing to print.')
        # if HashTable is not empty, print each bucket's LinkedList
        else:
            for i in range(0, self.size):
                # print contents of bucket if it's LinkedList is not empty
                if self.buckets_list[i].is_empty() is False:
                    print('Bucket number: ', i)
                    self.buckets_list[i].print_list()
        return

    # return a list of all keys
    def return_keys(self):
        # initialize a list of keys
        list_of_keys = []

        # iterate through buckets and append each key from each bucket
        for i in range(0, self.size):
            list_of_keys = list_of_keys + self.buckets_list[i].return_keys()

        return list_of_keys

        # [brian] for this you could write:

        list_of_keys = []

        for bucket in self.buckets_list:
            list_of_keys.extend(bucket.return_keys())

        return list_of_keys

    # return a list of all values
    def return_values(self):
        # initialize a list of values
        list_of_vals = []

        # iterate through buckets and append each value from each bucket
        for i in range(0, self.size):
            list_of_vals = list_of_vals + self.buckets_list[i].return_values()

        return list_of_vals

    # overloads [] operator so that d[key] will return the corresponding value
    # for key
    def __getitem__(self, key):
        # hash the key and find the correct LinkedList to search
        hashed_key = hash(key) % self.size
        bucket = self.buckets_list[hashed_key]

        # raise KeyError if bucket is empty
        if bucket.is_empty():
            raise KeyError('In HASHTABLE class: Searching incorrect list.')
        else:
            temp = bucket.search(key)
            if temp is not None:
                return temp.value
            else:
                raise KeyError('In HASHTABLE class: Key does not exist.')

if __name__ == '__main__':
    def test_node():
        # test Node class
        print('Testing Node class:')
        head = Node('head', 10)
        arm = Node('arm', 2)
        leg = Node('leg', 21)

        head.print_node()                       # should print 10
        arm.print_node()                        # should print 2
        leg.print_node()                        # should print 21

        head.set_value(7)
        arm.set_value(3)
        leg.set_value(13)

        print('Updated Nodes:')
        head.print_node()                       # should print 7
        arm.print_node()                        # should print 3
        leg.print_node()                        # should print 13

        print('Testing return_value function:')
        print('head', head.return_value())      # should print 7
        print('arm', arm.return_value())        # shold print 3
        print('leg', leg.return_value())        # should print 13
        return

    def test_linked_list():
        # test LinkedList class
        print('\nTesting LinkedList class:')
        body = LinkedList()

        print('Testing is_empty function:')
        if body.is_empty():
            print('is_empty() works!')  # should print

        print('Testing print_list function for empty LinkedList:')
        body.print_list()               # should print error message

        body.insert('head', 14)
        body.insert('arm', 6)
        body.insert('leg', 2)
        body.insert('eye', 13)
        body.insert('mouth', 9)

        print('Testing insert and print_list function:')
        body.print_list()               # should print 9, 13, 2, 6 14

        print('Testing search function:')
        reference_pointer1 = body.search('head')
        reference_pointer2 = body.search('leg')
        reference_pointer1.set_value(1)
        reference_pointer2.set_value(12)
        body.print_list()               # should print 12, 6, 1

        print('Testing search function for key not in LinkedList:')
        reference_pointer3 = body.search('chest')       # should print error

        print('Testing update_value function:')
        body.update_value('mouth', 20)
        body.update_value('head', 33)
        body.print_list()               # should print 20, 13, 2,  6, 33

        print('Testing update_value function for key not in LinkedList:')
        body.update_value('thigh', 2)   # should print two errors

        print('Testing delete function:')
        body.delete('arm')
        body.delete('head')
        body.delete('mouth')
        body.delete('leg')
        body.delete('eye')
        body.print_list()

        print('Create new list to delete')
        body.insert('hello', 23)
        body.insert('goodbye', 1)
        body.insert('morning', 19)
        body.insert('evening', 7)
        body.print_list()

        body.delete('evening')
        body.delete('hello')
        body.print_list()
        return

    def test_hash_table():
        # test HashTable class
        print('\nTesting HashTable class')
        # create a HashTable with 10 buckets
        test = HashTable(10)

        print('Testing print_hash_table for empty HashTable:')
        test.print_hash_table()             # print warning

        print('Testing insert function:')
        test.insert('blue', 3)
        test.insert('green', 14)
        test.insert('orange', 2)
        test.insert('yellow', 4)
        test.insert('gold', 1)
        test.insert('black', 23)
        test.insert('white', 31)
        test.insert('red', 2)
        test.insert('purple', 30)
        test.insert('brown', 22)
        test.insert('grey', 16)
        test.insert('silver', 8)
        test.print_hash_table()             # should print table

        print('Testing return_keys function')
        print(test.return_keys())
        print('Testing return_values function')
        print(test.return_values())

        print('Testing delete function:')
        test.delete('brown')
        test.delete('silver')
        test.print_hash_table()

        print('Testing return_num_of_items function:')
        print('Num of items: ', test.return_num_of_items())     # print 12

        print('Testing delete function:')
        test.delete('brown')
        test.delete('silver')
        test.print_hash_table()

        print('Testing get function:')
        print('Value of black is: ', test.get('black'))         # print 23
        print('Value of blue is: ', test.get('blue'))           # print 3
        print('Value of silver is: ', test.get('silver'))       # print 8
        print('Value of gray is: ', test.get('gray'))           # print error

        print('Testing update_value/overloaded assignment operator:')
        # test.update_value('orange', 15)
        test['orange'] = 15
        test.print_hash_table()

        print('Testing update_value function for non-existing key:')
        # test.update_value('gray', 33)
        test['gray'] = 33
        test.print_hash_table()

        print('Testing delete function:')
        test.delete('brown')
        test.delete('silver')
        test.print_hash_table()

        print('Testing return_keys function')
        print(test.return_keys())
        print('Testing return_values function')
        print(test.return_values())

        print('Testing overloaded [] operator')
        print('Value of orange is: ', test['orange'])
        print('Value of brown is: ', test['brown'])             # print error

        return

    # test_node()
    # test_linked_list()
    test_hash_table()
