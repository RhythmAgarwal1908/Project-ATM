class Atm:
    def __init__(self,card_number,pin):
        self.card_number=card_number,
        self.pin=pin
    def CashWithdrawl(self,amount):
        Money = 10000 - amount
        print("You Have"+str(Money)+"Left")
    def CheckBalance(self):
        print("You have 10000 Balance")

card_number=input("Please Enter Your Card Number")
pin=input("Please Enter Your Pin")


BankATM=Atm(card_number,pin)

print("Press 1 for Cash Withdrawl")
print("Press 2 for Balance Enquiry")

Transaction=int(input("Enter the Activity"))

if(Transaction==1):
    amount=int(input("How Amount You want to Withdraw"))
    BankATM.CashWithdrawl(amount)
elif(Transaction==2):
    BankATM.CheckBalance()
else:
    print("Enter The Valid Number")
    