
# Objective:
# Given two sets of integers, A and B, print their symmetric difference in ascending order.
# The symmetric difference includes elements that are in either A or B but not in both.

# read input (set m)
M=int(input())
set_M = set(map(int,input().split()))
# convert set m to list
set_M_to_list=list(set_M)

# read input (set n)
N=int(input())
set_N = set(map(int,input().split()))
# convert set n to list
set_N_to_list=list(set_N)

## merg two list
set_M_to_list.extend(set_N_to_list)
set_M_union_set_N = set_M_to_list

## sort the list 
set_M_union_set_N.sort()


symmetric_difference_list =[] 

for var in set_M_union_set_N:
    if var not in symmetric_difference_list:
        symmetric_difference_list.append(var)
    elif var in symmetric_difference_list:
        symmetric_difference_list.remove(var)   
        
for var in symmetric_difference_list:
    print(var) 
