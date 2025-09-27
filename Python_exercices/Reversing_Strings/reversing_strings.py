'''
* Create a program that reverses the order of characters in a text string
* without using built-in functions that do it automatically.
* For example, if the input is "Hola mundo" the output would be "odnum aloH"

'''

def reversing(string):
    i = len(string) - 1
    while i >= 0:
        print(string[i],end='')
        i -= 1

reversing("Hello World")
print()
reversing("How can i help you?")

     
    