#!/usr/bin/env python3

my_list = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]


def calculate_median(a_list):
    sorted_list = sorted(a_list)
    list_len = len(sorted_list)

    if list_len < 1:
        return None
    if list_len % 2 == 0 :
        first_index = (list_len - 1)//2
        second_index = (list_len + 1)//2
        
        return ( sorted_list[first_index] + sorted_list[second_index] ) / 2.0
    else:
        index = (list_len)//2
        return sorted_list[index]

def List_average(a_list):
    average = sum(a_list)/len(a_list)
    return average

def num_occu(a_list):
    most_occ = 0
    num = a_list[0]
    for i in a_list:
        
        if a_list.count(i)> most_occ:
            most_occ = a_list.count(i)
            num = i
            print(num)

            input()
    return num




print(calculate_median(my_list))

# print(List_average(my_list))

print(num_occu(my_list))