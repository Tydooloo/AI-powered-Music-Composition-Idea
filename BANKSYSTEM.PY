class BasicBankAccount:
    def __init__(self,account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("invalid transaction. Insufficient funds or negative amount entered.")

    def get_balance(self):
        return self.balance

class SavingsBankAccount(BasicBankAccount):
    def __init__(self, account_number, balance, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

class BankSystem():
    def __init__(self):
        self.bank_accounts = {}
        self.prefix_account = '123-'
        # key value dataset
        self.commands = {
            'A': 'creates bank account',
            'B': 'closes bank account',
            'C': 'deposit money on selected bank account', 
            'D': 'withdraw money on selected bank account',
            'E': 'Get the Balance of any bank account',
            'F': 'Exit the bank system'
        }

    def show_commands(self):
        print('Commands')
        print('-'*20)
        print('\n'.join(f'{k} | {v}' for k, v in self.commands.items()))
        print('-'*20)



    def create_account_number(self):
        account_number = self.prefix_account + str(len(self.bank_accounts))
        return account_number


    def make_account(self, balance, interest):
        new_account_number = self.create_account_number()
        account = SavingsBankAccount(new_account_number, balance, interest)
        self.bank_accounts[new_account_number] = account
        print(self.bank_accounts)

    def close_account(self, ID):
        account_to_delete = None
        for i in self.bank_accounts.keys():
            if i[4:] == str(ID):
                account_to_delete = i
                break
        if account_to_delete is not None:
            del self.bank_accounts[account_to_delete]
            print("deleted")
        else:
            print('Not found')
        print(self.bank_accounts)

    def deposit(self):
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to deposit: "))
        if account_number in self.bank_accounts:
            self.bank_accounts[account_number].deposit(amount)
            print(f"Deposited {amount} to account {account_number}.")
        else:
            print("Account not found.")

    def withdraw(self):
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to withdraw: "))
        if account_number in self.bank_accounts:
            self.bank_accounts[account_number].withdraw(amount)
            print(f"Withdrew {amount} from account {account_number}.")
        else:
            print("Account not found.")

    def get_balance(self):
        account_number = input("Enter the account number: ")
        if account_number in self.bank_accounts:
            balance = self.bank_accounts[account_number].get_balance()
            print(f"The balance of account {account_number} is {balance}.")
        else:
            print("Account not found.")


    def is_valid(self,command):
        all_commands = self.commands.keys()
        if len(command) != 1:
            return False
        elif command in all_commands:
            return True
        else:
            return False
    def show_bank_accounts(self):
        for i,a in enumerate(self.bank_accounts.keys()):
            print(a)


    def run(self):
        while True:
            self.show_commands()
            command = input('Enter you command').upper()
            if self.is_valid(command):
                if command ==  'F':
                    break
                elif command == 'A':
                    self.make_account(100, 0.01)
                elif command == 'B':
                    self.show_bank_accounts()
                    self.close_account(1)
                elif command == 'C':
                    self.show_bank_accounts()
                    self.deposit()
                elif command == 'D':
                    self.show_bank_accounts()
                    self.withdraw()
                elif command == 'E':
                    self.show_bank_accounts()
                    self.get_balance()
            else:
                print('please use valid commands')
        
        print('exit the program')
            
            



bank_system = BankSystem()
bank_system.run()








