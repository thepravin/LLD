from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance:int)->None:
        self.balance = balance

    @abstractmethod
    def deposite(self):
        pass

class WithdrawableAccount(BankAccount):
    @abstractmethod
    def withdraw(self):
        pass



class SavingAccount(WithdrawableAccount):
    def __init__(self,balance:int)->None:
        super().__init__(balance)

    def withdraw(self, amount)->None:
        if(amount > self.balance):
            print("Insufficent Balance...")
            return

        self.balance -= amount
        print(f"Withdraw successfully...!!!\n Current Balance is {self.balance} Rs.")

    def deposite(self, amount)->None:
        self.balance += amount
        print(f"Current balance is {self.balance} RS.")


class FixedDepositeAccount(BankAccount):
    def __init__(self,balance:int)->None:
        super().__init__(balance)

    def deposite(self, amount)->None:
        self.balance += amount
        print(f"Current balance is {self.balance} RS.")


if __name__ == "__main__":
    s = SavingAccount(5000)
    s.deposite(270)
    s.withdraw(2000)

    print("Fixed Deposite : ")

    fd = FixedDepositeAccount(2000)
    fd.deposite(456)
    # fd.withdraw(45) Error: FixedDepositeAccount dosen't have withdraw attrabute