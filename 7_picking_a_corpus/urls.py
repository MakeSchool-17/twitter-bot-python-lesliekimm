# hardcode the first part of the url
URL = 'http://www.5novels.com/classics/u5691_'


# method that will create urls for online version of the lord of the rings:
# fellowship of the rings book and output urls to a text file
def create_list_of_URLs():
    # open pages.txt as write only
    f = open('pages.txt', 'w')

    # this online version has the book on 146 different pages - iterate
    # 146 times to create urls and write each url to file
    for i in range(2, 50):
        # create specific url for page
        url_to_add = URL + str(i) + '.html'
        # write to file
        f.write(url_to_add)
        # write a newline to file
        f.write('\n')
