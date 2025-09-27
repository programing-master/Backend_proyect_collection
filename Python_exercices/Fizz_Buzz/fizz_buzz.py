# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number.
# For multiples of five print "Buzz" instead of the number.
# For numbers which are multiples of both three and five print "FizzBuzz".

def fizz_buzz():
    for i in range(1,101):
        result = f'{i} -> FizzBuzz' if i % 3 == 0 and i % 5 == 0 else \
                 f'{i} -> Fizz' if i % 3 == 0 else \
                 f'{i} -> Buzz' if i % 5 == 0 else \
                 str(f'{i} -> No match')
        print(result)

fizz_buzz()