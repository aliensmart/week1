#!/usr/bin/env python3

my_list = [1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]]
my_list2 = [1,2,3,4,5,6,7,8]

def list_iteration(my_list):
    for i in my_list:
        
        if type(i)==list:
            for l in i:
                print(l)
                if type(l)==list:
                    for n in l:
                        print(n)
        else:
            print(i)

list_iteration(my_list2)
