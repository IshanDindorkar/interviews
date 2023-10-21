from typing import List


def square(x):
    return x ** 2


def approach_use_map_function(numbers: List):
    squared_numbers = map(square, numbers)  # map() is an annonymous function
    return list(squared_numbers)


def approach_use_lambda(numbers: List):
    squared_numbers = map(lambda x: x ** 2, numbers)
    return list(squared_numbers)


def main():
    numbers = [2, 4, 6]

    # Approach 1: use of map function with a defined function called as "square"
    print(approach_use_map_function(numbers=numbers))

    # Approach 2: use of lambda function as anonymous funtion
    print(approach_use_lambda(numbers=numbers))


if __name__ == "__main__":
    main()

# EOF
