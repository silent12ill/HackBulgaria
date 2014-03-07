# Problem 8 - Number containing a single digit?
#
# Implement a function, called contains_digit(number, digit),
# which checks if digit is contained by the given number.
#
# digit and number are integers.
#
# Signature
#
# def contains_digit(number, digit):
#     # Implementation
#
# Test examples
#
# >>> contains_digit(123, 4)
# False
# >>> contains_digit(42, 2)
# True
# >>> contains_digit(1000, 0)
# True
# >>> contains_digit(12346789, 5)
# False


# FUNCTIONS
def contains_digit(number, digit):
    number = str(number)
    digit = str(digit)

    if digit in number:
        return True

    else:
        return False


# main
def main():
    print(contains_digit(123, 4))
    print(contains_digit(42, 2))
    print(contains_digit(1000, 0))
    print(contains_digit(12346789, 5))

# PROGRAM RUN
if __name__ == '__main__':
    main()
