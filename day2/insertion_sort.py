my_list = [1, 2, 0, 8, 4, 6, 12]

def insertion_sort(a_list):
    n = len(a_list)
    totale = 0
    for i in range(1, n):
        key = a_list[i]
        j = i-1
        while j>=0 and key > a_list[j]:
            a_list[j+1]=a_list[j]
            j -=1
            totale +=1
        a_list[j+1] = key
        print("total: {} list: {}".format(totale,a_list))
        input()

    return a_list, totale

print(insertion_sort(my_list))