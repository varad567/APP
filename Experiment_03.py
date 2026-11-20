"""
Experiment 03 - Configurable Payment Processing System using Strategy Pattern (CO-1)
"""
from abc import ABC, abstractmethod


# ---------- Strategy interface ----------
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# ---------- Concrete strategies ----------
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid Rs.{amount} using Credit Card ending with {self.card_number[-4:]}")


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI ID {self.upi_id}")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid Rs.{amount} using PayPal account {self.email}")


# ---------- Context ----------
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid amount.")
            return
        self.strategy.pay(amount)


if __name__ == "__main__":
    processor = PaymentProcessor(CreditCardPayment("1234567812345678"))
    processor.process_payment(1500)

    # Change payment method at runtime
    processor.set_strategy(UPIPayment("varad@upi"))
    processor.process_payment(750)

    processor.set_strategy(PayPalPayment("varad@example.com"))
    processor.process_payment(2000)

    processor.process_payment(-10)
