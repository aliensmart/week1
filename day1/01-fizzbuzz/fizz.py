#!/usr/bin/env python3

def fizz(num):
    for number in range(num):
        if number==0:
            continue
        if (number % 3) == 0 and (number % 5) == 0:
            print("fizzbuzz") 
        elif (number % 5) == 0:
            print("buzz") 
        elif (number % 3) == 0:
            print("fizz") 
        else:
             print(number)

fizz(20)