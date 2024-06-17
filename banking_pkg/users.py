from .account import Account

class User():
    
    def __init__(self, user_name: str, user_pin: str):
        self.name = user_name
        self.pin = user_pin

class BankAccountHolder(User):
    
    def __init__(self, user_name: str, user_pin: str):
        super().__init__(user_name, user_pin)
        self.account = Account(0)
        print(f"{self.name} has been registered with a starting balance of $0")
        
    def logout(self):
        print(f"Goodbye {self.name}!")
        exit()