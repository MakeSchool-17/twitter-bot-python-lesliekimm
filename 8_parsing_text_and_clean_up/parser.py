import unicodedata


def parse_text(source_text):
    file_to_read = open(source_text, 'r')
    file_string = file_to_read.read()
    file_string.replace('‘', "'")

    print(file_string)
    return


if __name__ == '__main__':
    URL = '../7_picking_a_corpus/corpus.txt'

    parse_text(URL)
