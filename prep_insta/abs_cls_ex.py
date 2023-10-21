"""
Abstract class example
"""


from abc import ABC, abstractmethod


class AbsClsEx(ABC):
    @abstractmethod
    def process(self):
        pass


class ImplCls1(AbsClsEx):
    def process(self):
        print("Implementation for class 1")


def main():
    obj_1 = ImplCls1()
    obj_1.process()

    # this code should fail, hence commented
    # abs_obj = AbsClsEx()
    # abs_obj.process()


if __name__ == "__main__":
    main()

# EOF


