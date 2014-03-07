# Problem 17 - Slope style score
#
# Slope style featured as a new snowboarding discipline in the Sochi 2014 Winter Olympics.
#
# To get a medal, you need to get maximum score from the judges.
#
# All judges give you a score - a floating point number between 0 and 100. When all scores are given, the final score is calculated by the following algorithm:
#
# Remove the largest and the smallest score. From the rest, take the average.
# Implement a function, called slope_style_score(scores) where scores is a list of floating point numbers.
#
# The function should calculate and return the final score, according to the algoritm above.
#
# The final score should be rounded to two decimal points. This means that if we get a score 94.66666666666667 it should be rounded to 94.66
#
# Signature
#
# def slope_style_score(scores):
#     # Implementation
#
# Test examples
#
# >>> slope_style_score([94, 95, 95, 95, 90])
# 94.66
# >>> slope_style_score([60, 70, 80, 90, 100])
# 80.0
# >>> slope_style_score([96, 95.5, 93, 89, 92])
# 93.5

# FUNCTIONS
def slope_style_score(list):
    maxElement = max(list)
    minElement = min(list)
    list.remove(maxElement)
    list.remove(minElement)
    return sum(list) / len(list)

# main
def main():
    print(slope_style_score([94, 95, 95, 95, 90]))
    print(slope_style_score([60, 70, 80, 90, 100]))
    print(slope_style_score([96, 95.5, 93, 89, 92]))

# PROGRAM RUN
main()