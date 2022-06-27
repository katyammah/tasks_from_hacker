import os
import re
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" 
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_url(filename):  # return list of urls, sorted into alphabetical order
    underbar = filename.index('_')
    servername = filename[(underbar + 1):]

    text = open(filename)
    paths = []
    for line in text:  # look for path names in each line of the open file
        path_match = (re.search(r'GET\s(\S+)\sHTTP', line))
        paths.append(path_match[1])

    urls = set()
    for path in paths:  # exclude links without strips of puzzle
        if 'puzzle' in path:
            urls.add('http://' + servername + '/' + path)
    return sorted(urls)


def read_url2(filename):  # another form of sorting for the second puzzle (by the second word)
    underbar = filename.index('_')
    servername = filename[(underbar + 1):]

    text = open(filename)
    paths = []
    for line in text:  # look for the path names in each line of the open file
        path_match = (re.search(r'GET\s(\S+)\sHTTP', line))
        paths.append(path_match[1])

    urls = set()
    for path in paths:  # exclude links without strips of puzzle
        if 'puzzle' in path:
            urls.add('http://' + servername + '/' + path)

    def sort_key(url):
        return url[-8:-4]

    newurls = sorted(urls, key=sort_key)
    return newurls


def download_images(list_of_urls, dest_dir):
    if not os.path.exists(dest_dir):  # create a directory
        os.mkdir(dest_dir)

    num = 0
    for url in list_of_urls:  # copy images in the created directory as jpg
        urllib.request.urlretrieve(url, os.path.join(dest_dir, ('img {0}.jpg'.format(num))))
        num += 1

    indexfilename = (os.path.join(dest_dir, 'index.html'))
    indexfile = open(indexfilename, 'w')  # create empty file html and full it
    indexfile.write('<html>\n<body>\n')
    imagesstrip = ''
    for i in range(num):
        imagesstrip += '<img src="img {0}.jpg">'.format(i)
    indexfile.write(imagesstrip)
    indexfile.write('\n</body>\n</html>')
    indexfile.close()


def main():  # the first puzzle
    for url in read_url('animal_code.google.com'):
        print(url)  # for self-test
    download_images(read_url('animal_code.google.com'), 'animaldir')


def main2():  # the second puzzle
    for url in read_url2('place_code.google.com'):
        print(url)
    download_images(read_url2('place_code.google.com'), 'placedir')


if __name__ == '__main__':
    main()
