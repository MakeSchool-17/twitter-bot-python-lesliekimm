# dual purpose file
# contains executable as well as module

import random

# create a list of possible quotes to select from
quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")


# define a method that can be called or utilized in a file that imports
# this file
def random_python_quote():
    # select a random index and return the value at that index in the list
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

# if being called from this file, execute the following
if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
