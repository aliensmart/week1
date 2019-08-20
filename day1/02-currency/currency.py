#!/usr/bin/env python3
def currency_converter(amount):
    amount = float(amount)
    #convert the amount into cents
    amount = amount * 100
    hund = amount//10000
    amount = amount % 10000
    fift = amount//5000
    amount = amount%5000
    ten = amount//1000
    amount = amount%1000
    one = amount//100
    amount = amount%100
    quarter = amount//25
    amount = amount%25
    dime = amount//10
    amount = amount%10
    nickel = amount//5
    amount = amount%5
    penny = amount//1
    print(f"{hund} $100\n{fift} $50\n{ten} $10\n{one}")
        
print(currency_converter(200))
