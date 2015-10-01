class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

    def set_key(self, key):
        self.key = key
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

myLL = LinkedList()
myLL.insert(13, 'hello')
myLL.insert(1, 'bye')
print(myLL.size)

temp = myLL.head
for i in range(0, myLL.size):
    print(temp.key, temp.value)
    temp = temp.next


class HashTable:
    def __init__(self, bucketsList=None, size=None):
        self.bucketsList = bucketsList
        self.size = size

    # def insert(self, word, frequency):


# set a key
# get a value
# update a value
# return list of all keys
# return list of all values
