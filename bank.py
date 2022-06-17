

class Account:
    bank="postbank"
    def __init__(self,acc_name,acc_number):
        self.acc_name=acc_name
        self.acc_number=acc_number
        self.acc_balance=0
        self.deposits=[]
        self.withdrawals=[]
        
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount must be greater than zero"
        else:
            self.acc_balance +=amount
        self.deposits.append(amount)
        return f"Hello {self.acc_name}, you have deposited {amount},and your new balance is {self.acc_balance}"


    def withdraw(self,amount):
         transaction = 100
         if(amount+transaction)>self.acc_balance:
            return f"Insufficient funds"

         elif(amount+transaction)<=0:
          return f"amount must be greater than 0"

         else:
          self.acc_balance -= (amount+transaction)
          self.withdrawals.append(amount)
          return f"Hello {self.acc_name}, you have withdrawn {amount}, and a transaction fee of {transaction} has been deducted to your account and your new balance now is {self.acc_balance}"
   
    def deposits_statement(self):
        for depo in self.deposits:
              print(f"your withdraw was:{depo}")

    def  withdrawals_statement(self):
        for withdrawal in self.withdrawals:
            print(f"your withdraw was:{withdrawal}")

    def current_balance(self):
       return(f"Hello{self.acc_name}, you curent balance is {self.acc_balance}")
