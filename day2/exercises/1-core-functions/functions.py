#!/usr/bin/env python3
# input() #allows user input/ This function first takes the input from the user and then evaluates the expression and return a string



#round()#returns a floating point that is a rounded version of the specified number, with the specified number of decimals
        #SYNTAX(numer*, digits)
round(15)
round(15.67)
print(round(50.28,1))
print(round(50.28))

# len(s) returns the length of an object

# sum(iterable*, start) iterable (list,tuple, dict etc), adds items of the givem iterable from left to right

numbers = [2.5, 3, 9]
print(sum(numbers))
print(sum(numbers, 10))

# map(funct, iterable) returns a list of the result after applying the given function to each item of a given iterable
def add(n):
    return n**3

result = list(map(add, numbers))
print(result)

# filter(funct, iter) returns un iterator were the items are filtered through a function to test if the item is true or false

def my_funct(x):
    if x<100:
        return True
te_re = list(filter(my_funct, result))
print(te_re)

import functools

# reduce(funct, iter) used to apply a particular function passed in its argument to all of the list element
def myf(x,y):
    return x+y

re = functools.reduce(myf, numbers)

print(re)

# all(iterable) returns true if all items in an iterable are true, otherwise its returns false
mylist = [2,1,0]
print(all(mylist))

# any(iterable) returns true if any item in the iterable are true
print(any(mylist))

# zip(*iterable) returns a an iterator of the tuple based on the iterable object
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 

mapped = list(zip(name, roll_no, marks))
print(mapped)

# enumerate(iterable*, star) adds counter to an iterable and returns it.
grocery = ['milk','bread', 'butter']
enum = enumerate(grocery)
enum2 = enumerate(grocery, 3)

print(list(enum))
print(list(enum2))


# range(star, stop, steps) returns a sequence of numbers, starting from 0 by default, and increments by 1,

# count() list.count(element) return the number of occurences of an element in a list

max(iterable, *iterables)



