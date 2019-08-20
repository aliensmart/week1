#!/usr/bin/env python3
def is_palindrome(word):
    word = word.lower()

    reverse = word[::-1]
    if word == reverse:
        print(True)
    else:
        print(False)

# is_palindrome("jeff")
is_palindrome("radar")