class Account:
    def __init__(self):
        self.cust_name = raw_input("cust_name:")
        self.acc_no = raw_input("acc_no:")
        self.open_bal = int(raw_input("open_bal:"))
    def deposit(self,amount):
        self.bal += amount
        print amount, " has been deposited."
        print "New balance: ",self.bal
    def acc_data(self):
        print "Customer Name: ", self.cust_name
        print "Account number:", self.acc_no
        print "Balance: ", self.bal
    def withdraw(self,amount):
        if self.bal >= amount:
            self.bal -= amount
            print amount, " has been withdrawed."
            print "New Balance: ",self.bal
        else:
            print "Not enough balance"
class Current(Account):
    def __init__(self):
        Account.__init__(self)
        self.bal = self.open_bal
        self.min_bal = 10000
        self.penalty = 0.1
    def withdraw(self, amount):
        Account.withdraw(self, amount)
        if self.bal < (self.min_bal/2):
            print "Account balance is much less than minimum balance."
            print "Rs.450 penalty  has been imposed."
            self.bal -= 450
            print "New Balance: ",self.bal
        elif self.bal < self.min_bal:
            print "Account balance is less than minimum balance."
            print "Rs.350 penalty  has been imposed."
            self.bal -= 350
            print "New Balance: ",self.bal
class Savings(Account):
    def __init__(self):
        Account.__init__(self)
        self.bal = self.open_bal
    def interest(self):
        rate = float(raw_input("Enter rate of interest in %:"))/100
        n = int(raw_input("Enter number of times interest is calculated per year:"))
        t = int(raw_input("Enter number of years:"))
        self.bal = self.bal*((1+(rate/n))**(n*t))
        print "Interest has been credited."
        print "New balance: ", self.bal
