def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check for divisors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


# Test the function
print(is_prime(2))   # True
print(is_prime(17))  # True
print(is_prime(4))   # False
print(is_prime(9))   # False
