class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("Rs. ", amount, "was debited")
        print("Total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs. ", amount, "was credited")
        print("Total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance    




acc1=account(100000,12345)
# print(acc1.balance)
# print(acc1.account_no)

acc1.debit(60000)    # monthly home Expenses
acc1.debit(20000)    # rent  home
acc1.credit(25000)   # other buisness 
