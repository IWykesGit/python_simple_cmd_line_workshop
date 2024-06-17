from .users import *
from typing import Dict

def display_header() -> None:
    print("\n======== Automated Teller Machine ========")

def register_user() -> BankAccountHolder:
    display_header()
    user_name = input("Enter name to register: ")
    
    while True:
        user_pin = input("Enter PIN: ")
        
        if (len(user_pin) != 4):
            print("PIN must be 4 characters long!")
        else:
            break
    
    return BankAccountHolder(user_name, user_pin)

def get_login_data() -> Dict[str, str]:
    display_header()
    name_to_validate = input("Enter username: ")
    pin_to_validate = input("Enter PIN: ")
    
    return {"username": name_to_validate, "pin": pin_to_validate}
    
def validate_login(user: BankAccountHolder, login_data: Dict[str, str]) -> bool:
    return (login_data["username"] == user.name) and (login_data["pin"] == user.pin)
        

def display_atm_menu(user: BankAccountHolder) -> None:
    display_header()
    print("User: " + user.name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
    
def get_selected_screen_number() -> int:
    screen_number = 0
    while screen_number < 1 or screen_number > 4:
        try:
            screen_number = int(input("Where would you like to go: "))
        except ValueError:
            print("Please enter an integer.")
        else:
            if (screen_number < 1) or (screen_number > 4):
                print("Please provide an integer between 1 and 4.")
            
    return screen_number