class BankAccount(object):
    def __init__(self, account_number, name, pin_number):
        self.status = "open"
        self.account_number = account_number
        self.name = name
        self.pin_number = pin_number
    
    def __repr__(self):
        return '{} {} {}'.format(self.account_number, self.name, self.pin_number)

    def get_balance(self):
        #check account status
        if self.status != "open":
            raise ValueError("Dear Customer, your account was closed")
        return self.balance

    def open(self, balance = 0):
        self.balance = balance
        return self.balance 

    def deposit(self, amount):
        #can't deposit into closed account
        if self.status == "closed":
            raise ValueError("Dear Customer, you can't make any deposit cause account was closed")
        #can't deposit negative amount
        if amount <=0:
            raise ValueError("Dear Customer, you can't deposit negative amount of money")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        #can't withdraw more than deposited
        if self.balance < amount:
            raise ValueError("Dear Customer, you can't withdrawal morethan your account balance")
        
        #can't withdraw negative money
        if amount < 0:
            raise ValueError("Dear Customer, you can't withdrawal negative amount of money")
        
        self.balance -= amount
        return self.balance

    def close(self):
        #close account 
        self.status = "closed"
        return self.status


b = BankAccount(12345, "janet", 22)
print(b.__repr__())