# Write a program in Python to implement the Quick Sort algorithm to sort a list of numbers in ascending order.
# Using recursion
def quick_sort(list):
    
    if len(list) <= 1:
        return list
    piv = list[0]
    lower = [ x for x in list[1:] if x <= piv ]
    higher = [ x for x in list[1:] if x > piv ]
    return quick_sort(lower) + [piv] + quick_sort(higher)


arr = [23,21,43,23,65,11,987,678,456]
result = quick_sort(arr)
print(result)