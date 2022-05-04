#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import string


def mimic_dict(filename):
    f = open(filename, 'r')
    text = []
    for line in f:
        text += line.strip('\n').strip(string.punctuation).lower().split()

    m_dict = {}
    for i in range(len(text)-1):
        if text[i] not in m_dict.keys():
            m_dict[(text[i])] = [(text[i + 1])]
        else:
            m_dict[(text[i])].append((text[i + 1]))
    return m_dict


print(mimic_dict('small.txt'))  # вывела на экран функцию с подставленным файлом в качестве аргумента


#  Как в следующую функцию mimic внести значение получившегося словаря из предыдущей функции (mimic_dict),
#  чтобы она автоматически в качестве аргумента подставлялась? я, получается, внутри функции её указала,
#  и для другого словаря функция не сработает
def mimic(mimic_dict, word):
    mimic_dict = mimic_dict('small.txt')
    for i in range(20):
        print(word)
        if word in mimic_dict.keys():
            nextword = random.choice(mimic_dict[word])
        else:
            nextword = random.choice(list(mimic_dict.keys()))
        word = nextword


mimic(mimic_dict, 'are')  # для примера запустила функцию


# Следующую функцию не использовала, тоже не поняла её..
# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  mimic(dict, '')


if __name__ == '__main__':
  main()
