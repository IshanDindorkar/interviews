"""
Decorator design pattern:
The Decorator design pattern is a structural design pattern that allows behavior
to be added to individual objects, either statically or dynamically, without
affecting the behavior of other objects from the same class.
It is a way to extend the functionality of classes in a flexible and reusable manner.
"""

from abc import ABC, abstractmethod

from loguru import logger


# *********************************************
# *************** Component *******************
# *********************************************
class AbsCoffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass


class SimpleCoffee(AbsCoffee):
    def __init__(self):
        self._cost = 5

    def get_cost(self):
        return self._cost


# *********************************************
# *************** Decorator *******************
# *********************************************
class CoffeeDecorator(AbsCoffee, ABC):
    def __init__(self, coffee: AbsCoffee):
        self._coffee = coffee    # Decorator holds the reference to component object


class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 2


class SugarDecorator(CoffeeDecorator, ABC):
    def get_cost(self):
        return self._coffee.get_cost() + 4


def main():
    simple_coffee = SimpleCoffee()
    logger.info(f"Cost of a simple coffee ${simple_coffee.get_cost()}")

    coffee_with_milk = MilkDecorator(coffee=simple_coffee)
    logger.info(f"Cost of a simple coffee with milk ${coffee_with_milk.get_cost()}")

    coffee_with_sugar = SugarDecorator(coffee=simple_coffee)
    logger.info(f"Cost of a simple coffee with sugar ${coffee_with_sugar.get_cost()}")

    coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(coffee=simple_coffee))
    logger.info(f"Cost of a simple coffee with milk and sugar ${coffee_with_milk_and_sugar.get_cost()}")


if __name__ == "__main__":
    main()

# EOF
