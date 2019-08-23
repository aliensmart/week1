#!/usr/bin/env python3
from collections import Counter

def count_words(filename):
    with open(filename) as f:
        file_name = f.read()
        list_words = file_name.split()
        couter = Counter(list_words)

        print(couter)


count_words("test.txt")