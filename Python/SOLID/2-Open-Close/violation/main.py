class PaymentProcessor:
    def pay(self, payment_method:str, amount:int):
        if(payment_method == "UPI"):
            print(f"Starting UPI transaction of RS. {amount}")
            print("UPI transaction fininshed")

        elif payment_method == "credit_card":
            print(f"Starting Credit Card transaction of RS. {amount}")
            print("Credit card transaction finished")


pay_p = PaymentProcessor()
pay_p.pay("credit_card", 500)