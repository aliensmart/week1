#!/usr/bin/env python3
def currency_converter(amount):
    if amount >100:
        hund_times = amount//100
        left_hun = amount%100
        if left_hun >10:
            ten_time = left_hun//10
            left_ten = left_hun%10
            if left_ten >=1:
                result = "{} $100\n {} $10\n {} $1".format(hund_times, ten_time, left_ten)
                return result
        
print(currency_converter(200))
