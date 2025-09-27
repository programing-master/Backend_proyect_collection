"""
    This function implements a knapsack algorithm where there are multiple objects
    of different weights with given quantities (example weights: 1, 2, 5, 10, 20, 50).
    The goal is to find the most optimal way to fill exactly the knapsack's capacity
    without leaving any space unused.

    The function uses a greedy approach, attempting to fill the knapsack from the heaviest
    available items down to the lightest, reducing the available quantity of each item
    used. 

    Parameters:
    - weight: the maximum capacity of the knapsack to fill.
    - weights: a dictionary where keys are the weights of the objects and values are the 
      quantities available for each weight.

    If it is not possible to fill the knapsack exactly with the available objects and quantities,
    the function prints "Imposible" indicating that an exact filling cannot be achieved.

    Note: This simple approach does not guarantee the absolute optimal solution for all cases, 
    but solves a common greedy variant.

    Example usage:
    weights = {1: 5, 2: 3, 5: 2, 10: 1, 20: 1, 50: 1}
    bag(23, weights)
"""



def bag(weight, weights):
    
    if weight <= 0:
        return None
    # Sort the available weights in ascending order (to iterate downwards by index)
    we = sorted(weights.keys)

    # Start from the heaviest object index
    index = len(we) - 1

    # While the knapsack capacity is not filled and we still have weights to consider
    while weight != 0 and index >= 0:
        # If current weight is heavier than remaining capacity OR none available, skip
        if we[index] > weight or weights[we[index]] == 0:
            index -= 1
            continue

        print(we[index])  # Print the used item's weight
        weight -= we[index]  # Decrease remaining capacity by this weight
        weights[we[index]] -= 1  # Decrease the available quantity of this weight

    # If after using available objects the knapsack isn't filled exactly
    if weight != 0:
        print("Imposible")

# Example weights with quantities
weights = {1: 5, 2: 3, 5: 2, 10: 1, 20: 1, 50: 1}
bag(100, weights.copy())
print('\n')
bag(0, weights.copy())
