class bank:
    def __init__(self):
        self.balance=0
    def credit(self,a):
        self.balance=self.balance+a
    def debit(self,b):
        self.balance=self.balance-b
    def acc_balance(self):
        return self.balance
b=bank()
b.credit(41241)
b.debit(500)
print(b.acc_balance())    


