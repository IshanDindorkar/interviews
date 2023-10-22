"""
Factory Design Pattern:
The Factory Method pattern defines an interface for creating an object
but lets subclasses alter the type of objects that will be created.
"""

from abc import ABC, abstractmethod

from loguru import logger


class AbsManufacturer(ABC):
    @abstractmethod
    def get_product(self):
        pass


class AmericanManufacturer(AbsManufacturer):
    def get_product(self):
        product = AmericanProduct()
        product.manufacture()

        return product


class AsianManufacturer(AbsManufacturer):
    def get_product(self):
        product = AsianProduct()
        product.manufacture()

        return product


class AbsProduct(ABC):
    @abstractmethod
    def manufacture(self):
        pass


class AmericanProduct(AbsProduct):
    def __init__(self):
        self._type = "American"

    def manufacture(self):
        logger.info("Building American car")

    @property
    def type(self):
        return self._type


class AsianProduct(AbsProduct):
    def __init__(self):
        self._type = "Asian"

    def manufacture(self):
        logger.info("Building Asian car")

    @property
    def type(self):
        return self._type


class CarFactory:
    manufacturers = {}

    @staticmethod
    def register_manufacturer(name, cls):
        CarFactory.manufacturers[name] = cls

    @staticmethod
    def build_car(car_type: str):
        manufacturer = CarFactory.manufacturers[car_type]
        car = manufacturer().get_product()

        return car


def main():
    CarFactory.register_manufacturer("American", AmericanManufacturer)
    CarFactory.register_manufacturer("Asian", AsianManufacturer)

    car_type = input("Which type of car would you like to build? American or Asian \n")
    car = CarFactory.build_car(car_type=car_type)
    logger.info(f"Type of built car: {car.type}")  # Validation that right type of car is manufactured!


if __name__ == "__main__":
    main()

# EOF
