import view
import model
import random

def run():
    model.load()
    view.welcome_menu()
    main_menu()

def main_menu():
    while True:
        
        selection = view.choice()
        
        if selection == "1":

            create_account()

        elif selection == "2":
            login()

        elif selection == "3" :
            return

def login():
    account_number = view.account_number()
    pin = view.get_pin()
    if pin == model.check_pin(account_number, pin):
        menu(account_number)
    else:
        print("wrong pin")
        main_menu()





def menu(account_number):
    while True:
        first_name = model.get_f_name(account_number)
        last_name = model.get_l_name(account_number)
        view.main_menu(account_number, first_name, last_name)
        selection = view.choice()

        if selection == "1":
            model.get_balance(account_number)

        elif selection == "2":
            witdraw = float(view.withdraw())
            model.withdraw_money(account_number,witdraw)
            money_left = model.balance(account_number)
            
            model.save()
            if money_left < 0:
                view.insuf()

        elif selection == "3":
            depo = float(view.deposit())
            model.add_amount(account_number, depo)
            model.save()
        elif selection == "4":
            model.save()
            return
        

def create_account():
    first_name = view.get_f_name()
    last_name = view.get_l_name()
    pin = view.get_pin()
    confirm_pin = view.pin_confirm(pin)
    if confirm_pin != pin:
        print("wrong pin")
        create_account()
    else:
        account_number = "N4321" + str(random.randint(100, 1000))

        model.new_account(account_number, first_name, last_name, confirm_pin)
        model.save()
        view.new_account(account_number)
        view.welcome_menu()
        main_menu()









if __name__ == "__main__":
    run()