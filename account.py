from user import User
class Account:
    def __init__(self, bsb, number, user):    
        self.bsb = bsb
        self.number = number
        self.user = User
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(str(amount)+" Deposited successfully")

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -=amount
            print("Withdraw sucessfully")
        else:
            print('insufficient funds')

    def printBalance(self):
        print('Balance: '+ str(self.balance))

    def getUserDetails(self):
        self.user.printUser()

    def printAccount(self):
        print('Account details: ')
        self.getUserDetails()
        print('BSB: '+ str(self.bsb))
        print('Number: '+ str(self.number))
        self.printBalance()


