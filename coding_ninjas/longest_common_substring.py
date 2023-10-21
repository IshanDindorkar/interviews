"""
Find the longest common substring (LCS)
"""


def find_common_substring(input_1: str, input_2: str):
    max_length = 0
    end_pos = 0

    m = len(input_1)
    n = len(input_2)

    # Initialize 2D array with zero
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, (m+1)):
        for j in range(1, (n+1)):
            if input_1[i - 1] == input_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i

    return max_length, end_pos


def main():
    input_1 = input("Enter first string: \n")
    input_2 = input("Enter second string: \n")

    max_length, end_pos = find_common_substring(input_1=input_1,
                                                input_2=input_2)
    print(input_1[end_pos - max_length:len(input_1)])


if __name__ == "__main__":
    main()

# EOF
