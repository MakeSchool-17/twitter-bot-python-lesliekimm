# import python_quote_v2 to access it's modules
import python_quote_v2

# assign imported file to a variable
imported_file = python_quote_v2

# main module
if __name__ == '__main__':
    # call method form imported_file
    quote = imported_file.random_python_quote()
    print(quote)
