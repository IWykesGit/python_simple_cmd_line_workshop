
class Account:
    
    def __init__(self, balance: float):
        self.balance = balance
        self.deposits = []
        self.withdraws = []
        
    def show_balance(self):
        print(f"Current Balance: ${self.balance:.2f}\n")
        
    def deposit(self):
        deposit_amount = -1
        while deposit_amount <= 0:
            try:
                deposit_amount = float(input("Enter a deposit amount: $").replace(',', ''))
            except ValueError:
                print("Please enter a number that denotes a monetary amount")
            else:
                if (deposit_amount <= 0):
                    print("Enter a deposit amount greater than zero.")
                
        self.deposits.append(deposit_amount)
        self.balance += deposit_amount
        self.show_balance()

    def withdraw(self):
        while True:
            try:
                withdraw_amount = float(input("Enter a withdraw amount: $").replace(',', ''))
            except ValueError:
                print("Please enter a number that denotes a monetary amount")
            else:   
                if (withdraw_amount > 0.00) and (withdraw_amount <= self.balance):
                    self.withdraws.append(withdraw_amount)
                    self.balance -= withdraw_amount
                    self.show_balance()
                    break
                elif (withdraw_amount == 0.00) or (withdraw_amount < 0.00):
                    print("Enter a withdraw amount greater than zero.")
                elif (withdraw_amount > self.balance):
                    print(f"Balance too low, you have a balance of ${self.balance} available to withdraw.")
    