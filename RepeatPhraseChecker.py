# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:49:12 2021

@author: dani
"""

# Insert parameters
phrase_length = 5
threshold_count = 3
manuscript = 'test'


# Import libraries
import string
from collections import Counter
import csv

# read raw text
if manuscript.endswith('.txt'):
    manuscript = manuscript[:-4]
with open(manuscript + '.txt', encoding='UTF-8') as f:
    text = f.read()


# format text
text = text.lower()     # creates lowercases
text = text.replace('\n',' ')   # removes line breaks
text = text.translate(str.maketrans('', '', string.punctuation))    # removes all punctuation

# generate ordered list of words
words = text.split(' ')
words = list(filter(None, words))   # delete empty list items (which can be created by the replace function above)


# generate list of phrases
phrases = []
for i in range(len(words)):
    try:
        p = ''
        for j in range(phrase_length):
            p = p + words[i+j] + ' '
        p.strip(' ')
        phrases.append(p)
    except IndexError:
        break


# count occurrence of each phrase; only keep if it exceeds threshold
c = Counter(phrases)
c = {x: count for x, count in c.items() if count >= threshold_count}


# write to csv
with open('PhraseCounter_' + manuscript +'.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow([f'Phrase (length {phrase_length})','Count'])
    w.writerows(c.items())




