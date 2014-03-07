# Problem 26 - Spam and Eggs
#
# This is a problem from the Python 2012 course in FMI
#
# You can see the original problem statement here - http://2012.fmi.py-bg.net/tasks/1
#
# Implement a function, called prepare_meal(number) which takes an integer and returns a string, generated by the following algorithm:
#
# Еggs:
#
# If there is an integer n, such that 3^n divides number and n is the largest possible, the result should be a string, containing n times spam
#
# For example:
#
# >>> prepare_meal(3)
# 'spam'
# >>> prepare_meal(27)
# 'spam spam spam'
# >>> prepare_meal(7)
# ''
# Spam:
#
# If number is divisible by 5, add and eggs to the result.
#
# For example:
#
# >>> prepare_meal(5)
# 'eggs'
# >>> prepare_meal(15)
# 'spam and eggs'
# >>> prepare_meal(45)
# 'spam spam and eggs'
# Notice that in the first case, there is no "and". In the rest - there is.
#
# Signature
#
# def prepare_meal(number):
#     # Implementation
# Test examples
#
# >>> spam_and_eggs(5)
# "eggs"
# >>> spam_and_eggs(3)
# "spam"
# >>> spam_and_eggs(27)
# "spam spam spam"
# >>> spam_and_eggs(15)
# "spam and eggs"
# >>> spam_and_eggs(45)
# "spam spam and eggs"
# >>> spam_and_eggs(7)
# ""

# FUNCTIONS
def prepare_meal(number):
    if number == 0:
        return ""

    outputString = ""

    if number % 5 == 0:
        if number % 3 != 0:
            return "eggs"

        outputString = "and eggs"

    while number % 3 == 0:
        outputString = "spam " + outputString
        number //= 3

    return outputString

# main
def main():
    print(prepare_meal(5))
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(15))
    print(prepare_meal(45))
    print(prepare_meal(7))

# PROGRAM RUN
if __name__ == '__main__':
    main()