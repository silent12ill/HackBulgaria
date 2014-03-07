# Problem 19 - Decreasing sequence?
#
# Implement a function, called is_decreasing(seq) where seq is a list of integers.
#
# The function should return True, if the given sequence is monotonously decreasing.
#
# And before you skip this problem, because of the math terminology, let me explain:
#
# A sequence is monotonously decreasing if for every two elements a and b,
# that are next to each other (a is before b), we have a > b
# For example, [5,4,3,2,1] is monotonously decreasing while [1,2,3,4,5,1] is not.
#
# Signature
#
# def is_decreasing(seq):
# Implementation
#
# Test examples
#
# >>> is_decreasing([5,4,3,2,1])
# True
# >>> is_decreasing([1,2,3])
# False
# >>> is_decreasing([100, 50, 20])
# True
# >>> is_decreasing([1,1,1,1])
# False

# FUNCTIONS


def is_decreasing(list):
    for i in range(len(list) - 1):
        if not list[i] > list[i + 1]:
            return False

    return True

# main
def main():
    print(is_decreasing([5, 4, 3, 2, 1]))
    print(is_decreasing([1, 2, 3]))
    print(is_decreasing([100, 50, 20]))
    print(is_decreasing([1, 1, 1, 1]))

# PROGRAM RUN
main()
