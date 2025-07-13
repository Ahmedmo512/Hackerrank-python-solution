# Task: Read an integer N and N space-separated integers.
# Create a tuple from the integers and print its hash value.
# Note: The output of hash() may vary between runs unless hash randomization is disabled.



# Enter your code here. Read input from STDIN. Print output to STDOUT

### Read input 
n = int(input())
input_list = input().split()

### convert input from str to int
input_list_int=map(int, input_list)

### convert map object to tuple
t=tuple(input_list_int)

## result of hash
print(hash(t))
