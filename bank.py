



class Account:
    bank="postbank"
    def __init__(self,acc_name,acc_number,amount,acc_balance):
        self.acc_name=acc_name
        self.acc_number=acc_number
        self.amount=amount
        self.acc_balance=acc_balance
        
    def deposit(self):
        self.acc_balance +=self.amount
        return self.acc_balance

    def withdraw(self):
        self.acc_balance -= self.amount
        return self.acc_balance