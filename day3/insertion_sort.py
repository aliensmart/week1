our_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 7, 7, 7, 7, 10, 10, 10, 10, 14, 14, 14, 14, 93, 93, 93, 93, 100, 100, 100, 100, 120, 120, 120, 120]

def insertion_sort(a_list):
    n = len(a_list)
    total = 0

    for i in range(1, n):
        key = a_list[i]
        j = i-1

        while j >= 0 and key > a_list[j]:
            a_list[j + 1] = a_list[j]
            j -= 1
            total += 1

        a_list[j + 1] = key
        #print("Total: {}, List:".format(total), a_list)
        #input()

    return a_list, total

print(insertion_sort(our_list))