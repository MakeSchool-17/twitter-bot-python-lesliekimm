import node


class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    # check if frequency is greater than parent and switch if it is all the
    # way to the root
    def bubble_up(self, pos):
        while pos // 2 >= 1:
            if self.heap_list[pos][1] > self.heap_list[pos // 2][1]:
                temp = self.heap_list[pos // 2]
                self.heap_list[pos // 2] = self.heap_list[pos]
                self.heap_list[pos] = temp
            pos //= 2

    # check if frequency is less than children and switch if it is all the
    # way down to the last leaf
    def bubble_down(self, pos):
        while (pos * 2) <= self.size:
            max_pos = self.max_child(pos)
            if self.heap_list[pos][1] < self.heap_list[max_pos][1]:
                temp = self.heap_list[pos]
                self.heap_list[pos] = self.heap_list[max_pos]
                self.heap_list[max_pos] = temp
            pos = max_pos
        pass

    # return the position of the child with the highest frequency
    def max_child(self, pos):
        if pos * 2 + 1 > self.size:
            return pos * 2
        elif self.heap_list[pos * 2][1] > self.heap_list[pos * 2 + 1][1]:
            return pos * 2
        else:
            return pos * 2 + 1

    # return key, value pair of top node
    def peek(self):
        return self.heap_list[1]

    # append to end of heap and bubble up to sort
    def insert(self, data):
        print(data)
        self.heap_list.append(data)
        self.size += 1
        self.bubble_up(self.size)

    # delete top and bubble down to sort
    def delete_max(self):
        max_pair = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.bubble_down(1)
        return max_pair
        pass

    # print heap
    def print_heap(self):
        current_index = 1
        while current_index <= self.size:
            pair = self.heap_list[current_index]
            print(pair)
            print('%10s' % pair[1], ' ', pair[0])
            current_index += 1


if __name__ == "__main__":
    def test_heap():
        my_heap = Heap()
        my_heap.insert(('orange', 10))
        my_heap.insert(('blue', 1))
        my_heap.insert(('yellow', 5))
        my_heap.insert(('purple', 15))
        my_heap.insert(('green', 5))
        my_heap.insert(('black', 7))
        my_heap.insert(('white', 12))
        my_heap.insert(('red', 5))

        my_heap.print_heap()

        print('testing delete:')
        my_heap.delete_max()
        my_heap.delete_max()

        my_heap.print_heap()

    test_heap()
