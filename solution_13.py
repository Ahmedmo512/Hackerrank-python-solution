# Task:
# Given multiple test cases, determine if one set A is a subset of another set B.

# Input:
# - First line: An integer T, the number of test cases.
# - For each test case:
#     - Line 1: Integer n (number of elements in set A)
#     - Line 2: n space-separated integers (elements of set A)
#     - Line 3: Integer m (number of elements in set B)
#     - Line 4: m space-separated integers (elements of set B)

# Output:
# - For each test case, print 'True' if A is a subset of B, otherwise print 'False'.



num_test=int(input())
output_list=[]

for i in range(num_test):
    num_element_set_A=int(input())
    set_A=set(map(int,input().split()))
    
    
    num_element_set_B=int(input())
    set_B=set(map(int,input().split()))
    
    if set_A.issubset(set_B):
        output_list.append(True)
    else:
        output_list.append(False)
        
for var in output_list:
    print (var) 
