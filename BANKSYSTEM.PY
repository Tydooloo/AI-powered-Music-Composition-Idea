import easygui


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
    

class BankAccountMgtSystem:
    def __init__ (self):
        self.accounts = {}
    
    def help(self):
        easygui.choicebox('Help', choices = ['help','help'])
    
    def create_account(self, name):
        account = BankAccount(1000)
        self.accounts[name] = account
        
    def delete_account(self, name):
        for account_name in self.accounts.keys():
            if account_name == name:
                self.accounts.pop(account_name)
        

    def print_all(self):
        output = ''
        for key, value in self.accounts.items():
            output += f'{key}:{value}'
        easygui.msgbox(output)
            



while True:
    a = BankAccountMgtSystem()
    options = [
    'help',
    'make new bank account',
    'delete bank account',
    'Print all',
    'Exit'
    ]

    choice =  easygui.buttonbox('Welcome to the bank', choices = options)
    if choice == 'help':
        a.help()
    if choice == 'make new bank account':
        a.create_account('Aarons account')
    if choice == 'delete bank account':
        a.delete_account()
    if choice == 'Print all':
        a.print_all()
    else:
        break
        
        
