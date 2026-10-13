from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount:int):
        pass


class UPI(PaymentMethod):
    def pay(self, amount:int):
            print(f"Starting UPI transaction of RS. {amount}")
            print("UPI transaction fininshed")


class PaymentProcessor:
     def process_payment(self, payment_method:PaymentMethod, amount:int):
          payment_method.pay(amount)

if __name__ == "__main__":
    pay_p = PaymentProcessor()

    upi = UPI()

    pay_p.process_payment(upi,500)
