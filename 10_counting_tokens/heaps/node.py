

class Node:
    # initialize Node object with data, l_child and r_child
    def __init__(self, data=None, l_child=None, r_child=None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child
        return

    # overload __str__ method to return Node content formatted to value
    # right aligned to 10 spaces followed by the key
    def __str__(self):
        node_string = '%10s' % self.data[1] + ' ' + self.data[0]
        return node_string

    # set key
    def set_key(self, key):
        self.data[0] = key
        return

    # return key
    def get_key(self):
        return self.data[0]

    # set value
    def set_value(self, value):
        self.data[1] = value
        return

    # return value
    def get_value(self):
        return self.data[1]

    # set data - key, value pair
    def set_data(self, data):
        self.data[0] = data[0]
        self.data[1] = data[1]
        return

    # return data - key, value pair
    def get_data(self):
        return self.data

    # set l_child pointer
    def set_l_child(self, l_child):
        self.l_child = l_child
        return

    # return l_child pointer
    def get_l_child(self):
        return self.l_child

    # set r_child pointer
    def get_r_child(self):
        return self.r_child

    # return r_child pointer
    def set_r_child(self, r_child):
        self.r_child = r_child
        return

    # print Node object formatted to value right aligned to 10 spaces
    # followed by the key - if not using overloaded __str__
    def print_node(self):
        print('%10s' % self.data[0], ' ', self.data[1])
        return

if __name__ == "__main__":
    def test_node():
        orange = Node(['orange', 3])
        blue = Node(['blue', 8])
        yellow = Node(['yellow', 1])
        purple = Node(['purple', 2])
        green = Node(['green', 9])
        black = Node(['black', 5])

        print(orange)
        print(blue)
        print(yellow)
        print(purple)
        print(green)
        print(black)

    test_node()
