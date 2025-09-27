
'''
This algorithm generates all subsets (the power set) of a given array representing a mathematical set using backtracking. At 
each step, it explores a binary decision—whether to include or exclude the
current element—forming a binary decision tree like the one below:

           Start (index=0, subset=[])
              |                   |
    Exclude 1 (index=1, [])    Include 1 (index=1, [1])
      |      |             |         |
Exclude 2   Include 2    Exclude 2  Include 2
 (2, [])     (2, [2])     (2, [1])   (2, [1, 2])
   |  |        |   |        |   |      |    
 
This tree captures the recursive backtracking process generating 
all possible subsets without repetition and ignoring order within
each subset. The empty set is also included as a valid subset.
The justification is mathematical: for a set of size 

subsets, since each element can either be included or excluded independently.

Thus, this backtracking approach systematically enumerates all 

  subsets by traversing a decision tree whose depth 
  is the size of the input set. Each path from the 
  root to a leaf represents one unique subset, ensuring 
  complete coverage of the power set.

'''

def subsets(list,index=0,subset=[]):
     if index == len(list):
       print(subset)
       return
     # not including the subset
     subsets(list,index + 1,subset)
     # including the subset
     subsets(list,index + 1,subset + [list[index]])
    
set = [1,2,3]
subsets(set)