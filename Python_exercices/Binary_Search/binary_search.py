# Write a program in Python that implements the binary search algorithm to find the position (index) of a given element in a list of integers.
# The list must be sorted in ascending order beforehand, since binary search only works correctly on sorted lists.
# You may use any sorting method of your choice to sort the list before performing the binary search.
# The program should take as input the sorted list and the element to search for,
# and return the index of the element if found, or indicate that it is not present in the list.


#We will choose bubble sort, so we will perform the corresponding function
def bubble_sort(list):
    n = len(list) - 1
    for i in range(n):
        for j in range(n - i):
            if list[j] > list[j+1]:
                list[j] , list[j+1] = list[j+1] , list[j]
    return list

def binary_search(list,objetive):
    n = len(list) 
    start=0
    end=n-1
    
    while start <= end:
        center = (start + end) // 2
        if list[center] == objetive:
             return center
        elif list[center] < objetive:
             start = center + 1
        else:
             end = center -1
    return None
         

#this is an original array
arr= [12,432,21,654,234,456,678,100,32,11]
#this is an order array
order_array=bubble_sort(arr)

print(binary_search(arr,456))
print(binary_search(arr,12))
print(binary_search(arr,11))
print(binary_search(arr,678))
