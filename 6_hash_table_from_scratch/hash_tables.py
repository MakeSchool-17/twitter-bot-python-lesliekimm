import hashlib

class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key                  # word
        self.value = value              # frequency
        self.next = None

    def set_key(self, key):
        self.key = key
        return

    def set_value(self, value):
        self.value = value
        return

    def return_value(self):
        return self.value


class LinkedList:
    def __init__(self, head=None, size=None):
        self.head = None
        self.size = 0

    def insert(self, key, value):
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return

    # searches list for a key and returns pointer to the Node
    def search(self, key):
        temp = self.head
        while temp.next is not None:
            if temp.key is key:
                return temp
            else:
                temp = temp.next
        if temp.key is key:
            return temp
        return

    def update_value(self, key, new_value):
        temp = self.head
        for i in range(0, self.size):
            if temp is not None:
                if temp.key is key:
                    temp.set_value(new_value)
                    break
                else:
                    temp = temp.next
        if temp is None:
            print('WARNING: In LINKEDLIST class: Key not found. Nothing ' +
                  'to update.')
        return

    # print the list, frequency followed by the word
    def print_list(self):
        temp = self.head
        while temp is not None:
            print('%10s' % temp.value, '  ', temp.key)
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


print('creating hash table')
myHT = HashTable(10)
for i in range(0, myHT.size):
    print(type(myHT.buckets_list[i]))
myHT.insert('green', 2)
myHT.insert('blue', 12)

for i in range(0, 10):
    if myHT.buckets_list[i].head is not None:
        myHT.buckets_list[i].print_list()
    else:
        print('empty bucket')

myHT.update_value('blue', 5)
myHT.update_value('yellow', 7)

for i in range(0, 10):
    if myHT.buckets_list[i].head is not None:
        myHT.buckets_list[i].print_list()
    else:
        print('empty bucket')

# testing
myLL = LinkedList()
myLL.insert('hand', 13)
myLL.insert('bye', 1)
myLL.insert('hello', 12)
myLL.insert('face', 20)
print(myLL.size)

temp = myLL.head
for i in range(0, myLL.size):
    print(temp.key, temp.value)
    temp = temp.next

myLL.update_value('hello', 14)
myLL.update_value('booger', 2)

print('after update')
temp = myLL.head
for i in range(0, myLL.size):
    print(temp.key, temp.value)
    temp = temp.next

tempA = myLL.search('face')
print('testing search', tempA.key, tempA.value)

# set a key
# return list of all keys
# return list of all values
