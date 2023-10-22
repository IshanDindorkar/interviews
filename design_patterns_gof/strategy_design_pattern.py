"""
Strategy design pattern:
The Strategy design pattern is a behavioral design pattern that defines a
family of interchangeable algorithms, encapsulates each one, and makes
them interchangeable. This pattern allows a client to choose an algorithm
from a family of algorithms at runtime. It promotes the "Open/Closed Principle"
by allowing new algorithms to be added without modifying existing client code.
"""

from abc import ABC, abstractmethod


class AbsPayment(ABC):
    @abstractmethod
    def pay(self, amount: int):
        pass


class DebitCardPayment(AbsPayment):
    def pay(self, amount: int):
        response = f"Payment for amount INR {amount} done using debit card"
        return response


class CreditCardPayment(AbsPayment):
    def pay(self, amount: int):
        response = f"Payment for amount INR {amount} done using credit card"
        return response


class OnlineBankingPayment(AbsPayment):
    def pay(self, amount: int):
        response = f"Payment for amount INR {amount} done using online banking"
        return response


class WalletPayment(AbsPayment):
    def pay(self, amount: int):
        response = "Payment for amount INR {amount} done using wallet"
        return response


class ShoppingCart:
    def __init__(self):
        self._items = {}
        self._payment_strategy = None

    @property
    def payment_mode(self):
        return self._payment_strategy

    def add_item(self, name, cost):
        self._items[name] = cost

    def calculate_total_amount(self):
        total = 0

        for cost in self._items.values():
            total += cost

        return total

    def set_payment_strategy(self, payment_strategy: AbsPayment):
        self._payment_strategy = payment_strategy


def main():
    shopping_cart = ShoppingCart()

    # Step 1: Add items to shopping cart
    shopping_cart.add_item("Banana", 20)
    shopping_cart.add_item("Apple", 120)
    shopping_cart.add_item("Butter", 70)
    shopping_cart.add_item("Eggs", 80)

    # Step 2: Calculate total amount of items in cart
    total = shopping_cart.calculate_total_amount()

    # Step 3: Set payment mode
    shopping_cart.set_payment_strategy(CreditCardPayment())

    # Step 4: Make the payment
    response = shopping_cart.payment_mode.pay(amount=total)
    print(response)


if __name__ == "__main__":
    main()

# EOF
