
'''
  There is a list of fruits, a list of their prices, 
  and a list of their quantities. Create a backtracking
  algorithm that generates all possible combinations between
  them, which is known as the Cartesian product. For example,
  given the list of fruits ['apple', 'banana', 'pear'], the list
  of prices , and the list of quantities , the algorithm should
  produce all combinations such as 
     ['apple', 100, 10], ['apple', 100, 20],
     ['apple', 100, 30], ['apple', 200, 10],
     ['apple', 200, 20], and so on
'''

def backtracking_combinations(arrays,index,current_combination,result):
    if index == len(arrays):
        result.append(current_combination[:])
        return
    for element in arrays[index]:
        current_combination.append(element)
        backtracking_combinations(arrays,index + 1,current_combination,result)
        current_combination.pop()

fruits=['Apple','Banana','Pear']
prize=[100,200,300]
available=[10,20,30]
arrays=[fruits,prize,available]
result=[]
backtracking_combinations(arrays,0,[],result)
for element in result:
    print(element)