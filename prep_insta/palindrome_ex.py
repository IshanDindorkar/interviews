def is_palindrome(sequence: str):
    reverse_sequence = sequence[::-1]
    return sequence == reverse_sequence


def main():
    sequence = input("Enter sequence: \n")
    print(is_palindrome(sequence=sequence))  # example of palindrome string - "radar"


if __name__ == "__main__":
    main()

# EOF
