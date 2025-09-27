# Write a program in Python to implement the Fibonacci's Sequence algorithm.
# Use recursion
# Example:

#       1 1 2 3 5 8 13 21
#input  0 1 4 2
#output 1 1 5 2


def fibo(index):
    if index == 0 or index == 1:
        return 1
    return fibo(index - 1) + fibo(index - 2)

print(fibo(0))
print(fibo(1))
print(fibo(4))
print(fibo(2))