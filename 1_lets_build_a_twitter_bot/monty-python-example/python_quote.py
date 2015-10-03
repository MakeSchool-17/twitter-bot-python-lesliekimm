# script that returns random MP quote
# can only be run as script b/c all lines of quote are executed

import random

# list of possible quotes
quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

# get a random index between 0 and 2
rand_index = random.randint(0, len(quotes) - 1)
# print the quote at the random index
print(quotes[rand_index])
