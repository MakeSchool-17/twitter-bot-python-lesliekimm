

# MadLibs class will take in words from the user and create a version of
# the Three Little Pigs story.
class MadLibs:
    # initial variables include the story title, author, arrays for the
    # story text and input_words and string of the entire story
    def __init__(self):
        self.title = 'Three Little Pigs'
        self.author = ''
        self.text = ['Once upon a time, there were three ',             # 0
                     ' pigs. One day, their mother said, "You\'re all grown',
                     ' up and must ',                                   # 1
                     ' on your own." So they left to ',                 # 2
                     ' their houses. The first little pig wanted only to ',
                     ' all day and quickly built his house out of ',    # 4
                     '. The second little pig wanted to ',              # 5
                     ' and ',                                           # 6
                     ' all day so he ',                                 # 7
                     ' his house with ',                                # 8
                     '. The third ',                                    # 9
                     ' pig knew the wolf lived nearby and worked hard to ',
                     ' his house out of ',                              # 11
                     '. One day, the wolf knocked on the first pig\'s ',
                     '. "Let me in or I\'ll ',                          # 13
                     ' your house down!" The pig didn\'t, so the wolf ',
                     ' down the ',                                      # 15
                     '. The wolf knocked on the second pig\'s ',        # 16
                     '. "Let me in or I\'ll blow your ',                # 17
                     ' down!" The pig didn\'t, so the wolf ',           # 18
                     ' down the house. Then the wolf knocked on the third ',
                     ' pig\'s door. "Let me in or I\'ll blow your house down!',
                     '" The little pig didn\'t so the wolf ',           # 20
                     ' and ',                                           # 21
                     '. He could not blow the house down.',             # skip
                     ' All the pigs went to live in the ',              # 22
                     ' house and they all ',                            # 23
                     ' happily ever after.']
        self.input_words = []

    # get name of user
    def get_author(self):
        self.author = input('What is your name? ')
        return

    # get missing words in story text
    def get_input_words(self):
        self.input_words.append(input('Give me an adjective: '))        # 0
        self.input_words.append(input('Give me a verb: '))              # 1
        self.input_words.append(input('Give me a verb: '))              # 2
        self.input_words.append(input('Give me a verb: '))              # 3
        self.input_words.append(input('Give me a plural noun: '))       # 4
        self.input_words.append(input('Give me a verb: '))              # 5
        self.input_words.append(input('Give me a verb: '))              # 6
        self.input_words.append(input('Give me a past tense verb: '))   # 7
        self.input_words.append(input('Give me a plural noun: '))       # 8
        self.input_words.append(input('Give me an adjective: '))        # 9
        self.input_words.append(input('Give me a verb: '))              # 10
        self.input_words.append(input('Give me a plural noun: '))       # 11
        self.input_words.append(input('Give me a noun: '))              # 12
        self.input_words.append(input('Give me a verb: '))              # 13
        self.input_words.append(input('Give me a past tense verb: '))   # 14
        self.input_words.append(input('Give me a noun: '))              # 15
        self.input_words.append(input('Give me a noun: '))              # 16
        self.input_words.append(input('Give me a noun: '))              # 17
        self.input_words.append(input('Give me a past tense verb: '))   # 18
        self.input_words.append(input('Give me an adjective: '))        # 19
        self.input_words.append(input('Give me a past tense verb: '))   # 20
        self.input_words.append(input('Give me a past tense verb: '))   # 21
        self.input_words.append(input('Give me a noun: '))              # 22
        self.input_words.append(input('Give me a past tense verb: '))   # 23
        return

    # return string of the entire story with input form user
    def __str__(self):
        full_story = ''
        full_story += self.text[0]
        full_story += self.input_words[0]
        full_story += self.text[1] + self.text[2]
        full_story += self.input_words[1]
        full_story += self.text[3]
        full_story += self.input_words[2]
        full_story += self.text[4]
        full_story += self.input_words[3]
        full_story += self.text[5]
        full_story += self.input_words[4]
        full_story += self.text[6]
        full_story += self.input_words[5]
        full_story += self.text[7]
        full_story += self.input_words[6]
        full_story += self.text[8]
        full_story += self.input_words[7]
        full_story += self.text[9]
        full_story += self.input_words[8]
        full_story += self.text[10]
        full_story += self.input_words[9]
        full_story += self.text[11]
        full_story += self.input_words[10]
        full_story += self.text[12]
        full_story += self.input_words[11]
        full_story += self.text[13]
        full_story += self.input_words[12]
        full_story += self.text[14]
        full_story += self.input_words[13]
        full_story += self.text[15]
        full_story += self.input_words[14]
        full_story += self.text[16]
        full_story += self.input_words[15]
        full_story += self.text[17]
        full_story += self.input_words[16]
        full_story += self.text[18]
        full_story += self.input_words[17]
        full_story += self.text[19]
        full_story += self.input_words[18]
        full_story += self.text[20]
        full_story += self.input_words[19]
        full_story += self.text[21] + self.text[22]
        full_story += self.input_words[20]
        full_story += self.text[23]
        full_story += self.input_words[21]
        full_story += self.text[24] + self.text[25]
        full_story += self.input_words[22]
        full_story += self.text[26]
        full_story += self.input_words[23]
        full_story += self.text[27]
        return full_story

    # prints entire Mad Lib
    def print_all(self):
        print(self.title)
        print('Author: ', self.author)
        story = self.__str__()
        print(story)
        print('The end!')
        return


if __name__ == '__main__':
    my_story = MadLibs()
    my_story.get_author()
    my_story.get_input_words()
    my_story.print_all()
