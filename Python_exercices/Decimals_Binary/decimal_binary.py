# Implement a function that converts a decimal number to its corresponding binary number.

def decimal_binary(number):
     if number > 1:
         decimal_binary(number // 2)
     print(number % 2,end="")
     
decimal_binary(12)
print()
decimal_binary(122)

    