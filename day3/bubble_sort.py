our_list = [4, 7, 2, 10, 14, 93, 100, 1, 3, 120, 4, 7, 2, 10, 14, 93, 100, 1, 3, 120, 4, 7, 2, 10, 14, 93, 100, 1, 3, 120, 4, 7, 2, 10, 14, 93, 100, 1, 3, 120]

def bubble_sort(a_list):

    n = len(a_list)
    total = 0

    for i in range(n):

        for j in range(0, n-i-1):

            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

            total += 1
            #print("Total: {}, List: {}".format(total, a_list))
            #input()

    return a_list, total

print(bubble_sort(our_list))
