"""
Fibonacci series implementation
"""


def fibonacci(num_series: int):
    fib_series = []

    a, b = 0, 1
    while len(fib_series) < num_series:
        fib_series.append(a)  # append only one element at a time
        a, b = b, a + b

    return fib_series


def main():
    num_series = int(input("Enter num of elements in fibonacci series \n"))
    fib_series = fibonacci(num_series=num_series)
    print(fib_series)


if __name__ == "__main__":
    main()

# EOF
