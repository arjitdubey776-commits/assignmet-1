class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance = self.__balance - amount
            print("Withdrawal successful")

atm = ATM(5000)
atm.check_balance()
atm.deposit(1000)
atm.withdraw(2000)
atm.check_balance()
