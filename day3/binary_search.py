

def binary_search(a_list, l, r, x):
    total = 0

    while l <= r:
        total += 1
        mid = round(l + (r - l)/2)

        if a_list[mid] == x:
            return mid, total
        elif a_list[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False, total

our_list = [1, 2, 4, 7, 10, 14, 93, 100, 213,213,213,213,213,213,213,213,213,213,213,213,213,213]

result = binary_search(our_list, 0, len(our_list)-1, 1)
print(result)
