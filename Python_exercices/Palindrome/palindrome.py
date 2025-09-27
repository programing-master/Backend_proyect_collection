# Implement a function to determine if a word is a palindrome.
# A word is a palindrome when it reads the same forwards and backwards,
# case insensitive (i.e., 'Racecar' and 'racecar' are palindromes).

def palindrome(string):     
     n = len(string) - 1
     i = 0
     while i <= n // 2: 
         if string[i].lower() != string[n - i].lower():
             return False
         i += 1
     return True        

print(palindrome('racecar'))    # True (Palindrome)
print(palindrome('RaceCar'))    # True (Case insensitive)
print(palindrome('python'))     # False (Not palindrome)
print(palindrome('Level'))      # True
print(palindrome('World'))      # False