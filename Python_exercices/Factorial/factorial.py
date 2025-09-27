# Write a program in Python to implement the number factorial algorithm.
# Use recursion
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

print(factorial(5))
print(factorial(4))
print(factorial(3))