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
