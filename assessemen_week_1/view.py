def welcome_menu():
    print("Welcom to Terminal Teller")
    print("1) create account")
    print("2) log in")
    print("3) quit")

def new_account(account_number):
    print()
    input("First Name: ")
    input("Last Name: ")
    input("PIN: ")
    input("Confirm Pin")
    print(f"account created, your account number is {account_number}")

def choice():
    print()
    input("your choice: ")
    input()

def login():
    print()
    input("Account number: ")
    input("Pin: ")

def main_menu(customer_name, account_number):
    print()
    print(f"hello, {customer_name} ({account_number}) ")
    print("1) check balance")
    print("2) withdraw fund")
    print("3) deposit funds")
    print("4) sign out")

def withdraw(amount):
    print()
    print(f"how much to withdraw : {amount}")

def deposit(amount):
    print(f"How much to deposit: {amount}")


if __name__ == "__main__":
    welcome_menu()























