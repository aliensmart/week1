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
    with open(DATAPATH) as f:
        json.dump(data, f, indent=3)

def add_amount(account_number, amount):
    balance = data[account_number]["balance"]
    return balance + amount

def withdraw_money(account_number, amount):
    balance = data[account_number]["balance"]
    return balance - amount

def add_account(account_number):
    data[account_number] = {}


if __name__ == "__main__":
    load()
    add_account("N503531")
