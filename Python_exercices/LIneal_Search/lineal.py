# Write a program in Python to implement the Lineal Search algorithm.
# Use recursion 

# recursion
def lineal_search_recursion(list,element,position):
     if position < 0 or position > len(list) -1:
        return None
     if list[position] == element:
         return position
     return lineal_search_recursion(list,element,position + 1)
 

arr = [12,34,12,21,54,23,56]
print(lineal_search_recursion(arr,21,0))

     