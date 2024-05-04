class BankAccount():
    def __init__(self, balance):
        self.balance = balance
        print(f'initial {self.balance}')

    def deposit(self,amount):
        if amount < 0:
            print('please choose withdraw instead')
        else:
            self.balance += int(amount)


    def withdraw(self, amount):
        if amount < 0:
            print('please choose deposit instead')
        elif amount > self.balance:
            return
        else:
            self.balance -= int(amount)

    def get_balance(self):
        print(f'final price: {self.balance}')

class SavingsAccount(BankAccount): 
    def __init__(self, balance, interest_rate):
        super().__init__(balance) 
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance += self.balance*self.interest_rate
        return self.balance
    
savings = SavingsAccount(1000, 0.01)
savings.deposit(100)
savings.withdraw(200)
savings.apply_interest()
savings.get_balance()


