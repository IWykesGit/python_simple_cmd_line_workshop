from banking_pkg import bank
from time import sleep

user = bank.register_user()

while True:
    login_data = bank.get_login_data()
    if (bank.validate_login(user, login_data)):
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
        
while True:
    bank.display_atm_menu(user)
    user_selected_screen = bank.get_selected_screen_number()
    
    match user_selected_screen:
        case 1:
            user.account.show_balance()
        case 2:
            user.account.deposit()
        case 3:
            user.account.withdraw()
        case 4:
            user.logout()
    
    #fake loading
    sleep(2)
    


        

        