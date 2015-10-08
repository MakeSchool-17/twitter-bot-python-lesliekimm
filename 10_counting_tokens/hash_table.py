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
        random_index = random.randint(0, self.current_end_index)
        print(random_index)

        # iterate through distribution and if the random_index is less than
        # the index's current_end_index, return the index's key and break
        for index in range(len(distribution)):
            if random_index < distribution[index][1]:
                random_word = distribution[index][0]
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
