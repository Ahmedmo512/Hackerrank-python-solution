# Task:
# Given an integer n and n space-separated integers, create a tuple of those integers.
# Then compute and print the hash value of the tuple using Python's built-in hash() function.

# Input:
# - First line: An integer n, the number of elements in the tuple.
# - Second line: n space-separated integers.

# Output:
# - Print the hash value of the created tuple.

### Read input 
n = int(input())
input_list = input().split()

### convert input from str to int
input_list_int=map(int, input_list)

### convert map object to tuple
t=tuple(input_list_int)

## result of hash
print(hash(t))

n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))
