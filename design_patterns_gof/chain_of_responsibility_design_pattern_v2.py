"""
Chain of responsibility:
The Chain of Responsibility is a behavioral design pattern that is used to pass
requests along a chain of handlers. When a request is sent, it is processed by
one handler, and if that handler cannot or should not handle the request, it is
passed to the next handler in the chain, and so on, until the request is either
processed or discarded.
"""

import enum
from abc import ABC, abstractmethod

from loguru import logger


class EnumTaskStatus(enum.Enum):
    TakeOrder = 1
    Payment = 2
    PrepareOrder = 3
    Packing = 4


class Task:
    def __init__(self, desc=""):
        self._status = None
        self._desc = desc

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status


class AbsProcessor(ABC):
    @abstractmethod
    def process(self, task):
        pass


class GetOrder(AbsProcessor):
    def __init__(self):
        self._successor = None

    def set_successor(self, successor: AbsProcessor):
        self._successor = successor

    def process(self, task):
        if task.status is None:
            task.status = EnumTaskStatus.TakeOrder
            logger.info(f"Taking order is completed!")
        elif self._successor is not None:
            self._successor.process(task)
        else:
            logger.warning("End of road!")


class OrderPayment(AbsProcessor):
    def __init__(self):
        self._successor = None

    def set_successor(self, successor: AbsProcessor):
        self._successor = successor

    def process(self, task):
        if task.status == EnumTaskStatus.TakeOrder:
            task.status = EnumTaskStatus.Payment
            logger.info(f"Payment is completed!")
        elif self._successor is not None:
            self._successor.process(task)
        else:
            logger.warning("End of road!")


class OrderPreparation(AbsProcessor):
    def __init__(self):
        self._successor = None

    def set_successor(self, successor: AbsProcessor):
        self._successor = successor

    def process(self, task):
        if task.status == EnumTaskStatus.Payment:
            task.status = EnumTaskStatus.PrepareOrder
            logger.info(f"Order preparation is completed!")
        elif self._successor is not None:
            self._successor.process(task)
        else:
            logger.warning("End of road!")


class OrderPacking(AbsProcessor):
    def __init__(self):
        self._successor = None

    def set_successor(self, successor: AbsProcessor):
        self._successor = successor

    def process(self, task):
        if task.status == EnumTaskStatus.PrepareOrder:
            task.status = EnumTaskStatus.Packing
            logger.info(f"Order packing is completed!")
        elif self._successor is not None:
            self._successor.process(task)
        else:
            logger.warning("End of road!")


def main():
    task = Task(desc="Order food")

    get_order = GetOrder()
    order_payment = OrderPayment()
    prepare_order = OrderPreparation()
    pack_order = OrderPacking()

    get_order.set_successor(order_payment)
    order_payment.set_successor(prepare_order)
    prepare_order.set_successor(pack_order)

    task.status = EnumTaskStatus.PrepareOrder
    get_order.process(task=task)


if __name__ == "__main__":
    main()

# EOF
