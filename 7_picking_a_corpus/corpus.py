import requests
import urls
import datetime

imported_urls_file = urls

# diffbot API to use
DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
# user token
DIFFBOT_DEV_TOKEN = 'fc90bb8a5c45908f3f5720d88174522e'
# file containing all URLs
LIST_OF_URLS = 'pages.txt'


# return text from articule_url passed in as an argument
def get_article(article_url):
    # set request params for API request
    params = {'token': DIFFBOT_DEV_TOKEN,
              'url': article_url,
              'discussion': 'false'}
    # [brian] Nice! Making a dict before passing it in to another function,
    # while not necessary, makes the code to much easier to read

    print(params)

    res = requests.get(DIFFBOT_API_URL, params)     # hit the Diffbot API
    res_obj = res.json()['objects'][0]              # parse the response object
    return res_obj['text']                          # pull out the text


if __name__ == '__main__':
    # write 145 URLs that make up lord of the rings to pages.txt file
    imported_urls_file.create_list_of_URLs()
    # open text file or URLs
    urls_file = open(LIST_OF_URLS)
    # create corpus.txt file to write text to
    output_file = open('corpus.txt', 'w')

    corpus = ''                                     # initialize to empty

    print(datetime.datetime.now())

    # iterate through each line in urls_file and strip line of whitespace,
    # call get_article() with the line URL and add text to corpus string
    for line in urls_file:
        url = line.strip()
        article = get_article(url)
        corpus += article

    output_file.write(corpus)                       # write corpus to file

    # [brian] Careful, you forgot to close the file! In this program it'll get
    # closed when the script finishes, but in a larger program this could be a
    # pretty terrible mistake! Try writing:

    with open('corpus.txt', 'w') as output_file:
        output_file.write(corpus)
        print('Corpus saved to {}'.format(output_file.name))

    # and by the time the program reaches this line, the file will already
    # be closed.


    # print diagnostics
    print('Corpus saved to {}'.format(output_file.name))
    print(datetime.datetime.now())
