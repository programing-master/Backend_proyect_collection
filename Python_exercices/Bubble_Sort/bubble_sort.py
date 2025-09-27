# Write a program in Python to implement the Bubble Sort algorithm to sort a list of numbers in ascending order.
# The program should take an unsorted list, repeatedly compare adjacent elements, and swap them if they are in the wrong order.
# Finally, it should print the sorted list.
# The goal is to understand and apply the basic functioning of the Bubble Sort algorithm,
# which performs multiple passes to "bubble" the largest values to the end of the list via successive swaps.


def bubble_sort(list):
    n = len(list)
    if n < 0:
        return None
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j] , list[j+1] = list[j+1] , list[j]
    return list
                
arr = [45,43,21,12,67,54,123,543,765,897]
print(bubble_sort(arr))            