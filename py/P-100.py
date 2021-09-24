from typing import DefaultDict


class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your balanceis:$150")

    def cashwithdrawal(self,amount):
        new_amount = 100-amount
        print("You withdrawed: "+ str(amount)+ "Your remaining balanceis: " + str(new_amount)

def main():
        name = input("Hello what is your name?")
        print("Hello,"+name)
        cardnumber = input("input yard number: ")
        pin = input("Enter your pin: ")
        new_user = Atm(cardnumber,pin)

        print("Choose your activity")
        print("1.Balance Inquiry")
        print("2. Cash Withdrawal")
        activity = int(input("Enter activity choice: "))

        if(activi==1):
            new_user.balanceinquiry()
        elif (activiti ==2):
            amount = int(input("Enter the amount: "))
            new_user.cashwidthdrawal(amount)
            else:
                print("Enter a vaid number")

is __name__ == "__main":
main()