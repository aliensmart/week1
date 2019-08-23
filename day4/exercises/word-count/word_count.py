#!/usr/bin/env python3
from collections import Counter
# write a function count_words(filename)



def count_words(filename):
    with open(filename) as f:
        file_name = f.read()
        file_name = file_name.lower()
        list_words = file_name.split()
        couter = Counter(list_words)

        print(couter)


count_words("test.txt")