import json
import os

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}

def load():
    global data
    with open(DATAPATH) as j_file :
        data = json.load(j_file)

def save():
    with open(DATAPATH, "w") as f:
        json.dump(data, f, indent=3)

def add_amount(account_number, amount):
        data[account_number]["balance"] += amount

def withdraw_money(account_number, amount):
        data[account_number]["balance"] = data[account_number]["balance"] - amount

def balance(account_number):
        balance = data[account_number]["balance"]
        return balance 

def get_balance(account_number):
        balance = data[account_number]["balance"]
        print(balance)

def get_f_name(account_number):
        name = data[account_number]["first Name"]
        return name

def get_l_name(account_number):
        name = data[account_number]["Last Name"]
        return name

def check_pin(account_number, pin):
        pin = data[account_number]["pin"]
        return pin

def account_name(account_number):
      return  data[account_number]["first Name"]

def new_account(account_number, first_name, last_name, pin, balance=0):
        data[account_number] = {}
        data[account_number]["first Name"] = first_name
        data[account_number]["Last Name"] = last_name
        data[account_number]["pin"] = pin
        data[account_number]["balance"] = balance


if __name__ == "__main__":
    load()
#     add_account("N503531")
