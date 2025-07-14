# Task:
# You are given an initial set A, followed by a number of other sets.
# Each of the other sets comes with a mutation operation that needs to be 
# performed on A.
# Your goal is to perform all the specified mutation operations in order 
# and finally print the sum of the elements remaining in set A.

# Input Format:
# - The first line: An integer n, the number of elements in set A.
# - The second line: n space-separated integers — the elements of set A.
# - The third line: An integer m, the number of other sets and operations.
# - For each of the next m operations (2 lines each):
#     - First line: A string operation_name and an integer k 
#       (number of elements in the other set)
#     - Second line: k space-separated integers representing the other set.

# Available Set Mutation Operations:
# - update:                     A.update(B)
# - intersection_update:       A.intersection_update(B)
# - difference_update:         A.difference_update(B)
# - symmetric_difference_update: A.symmetric_difference_update(B)

# Output Format:
# - A single integer: the sum of elements in set A after all operations.


num_element_set_A = int(input())  # Read  number of element set A
set_A = set(map(int, input().split())) # Read  elements of set A 
num_of_other_set = int(input())  # Read the number of other sets 


for i in range(num_of_other_set):
    
    # Read the operation type and the size of the next set
    user_input = input().split() 
    
    methode = user_input[0]            # The name of the set method
    set_element = int(user_input[1])   # Number of elements in the next set 

    set_B = set(map(int, input().split()))
  
    getattr(set_A, methode)(set_B) # call the method on set_A using getattr


print(sum(set_A))
