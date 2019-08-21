
def sum_of_divisore(num):
    list_divisor = []

    for i in range(num+1):
        try:
            if num % i == 0 :
                list_divisor.append(i)
        except ZeroDivisionError:
            print('')
    sum_list_divisor = sum(list_divisor)
    number_of_list_divisor = len(list_divisor)
    sum_divisor = [list_divisor, sum_list_divisor, number_of_list_divisor]

    print(sum_divisor)

sum_of_divisore(76)