# Node class creates objects with data and next variables
class Node:
    # creates Node object with data and next parameters passed in
    # data is a list of string key and int value - ['key', value]
    def __init__(self, data=None, next=None):
        self.data = data                    # iniitalize data
        self.next = next                    # initialize next

    # return formatted output method to return data[1] (value) align right in
    # 10 spaces followed by the data[0] (key)
    def __str__(self):
        str_to_return = '%10s' % self.data[1] + '  ' + self.data[0]
        return str_to_return
