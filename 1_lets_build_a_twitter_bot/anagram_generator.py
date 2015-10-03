import random


# AnagramGenerator class takes a word from the user and scrambles the letters
class AnagramGenerator:
    def __init__(self):
        self.word = None

    # gets a word from the user
    def get_word(self):
        self.word = input('Please enter a word: ')
        return

    # shuffles the letters of the input word
    def create_anagram(self):
        # shuffle the letters and put into array
        shuffled_anagram = random.sample(self.word, len(self.word))
        # initialize empty string
        anagram = ''

        # go through shuffled_anagram array and concatenate all letters
        for i in range(0, len(self.word)):
            anagram += shuffled_anagram[i]
        return anagram

if __name__ == '__main__':
    my_anagram = AnagramGenerator()
    my_anagram.get_word()
    output = my_anagram.create_anagram()
    print(output)
