# Task:
# 1. Generate the first n Fibonacci numbers (starting from 0).
# 2. Cube each number using the map() function and a lambda expression.
# 3. Print the final list of cubed Fibonacci numbers.

# Input:
# An integer n (number of Fibonacci terms to generate)

# Output:
# A list of the cubes of the first n Fibonacci numbers.

# Example:
# Input: 5
# Fibonacci: [0, 1, 1, 2, 3]
# Cubed:     [0, 1, 1, 8, 27]



cube = lambda x: x*x*x # lambda expression to cube each fibonacci numbe

def fibonacci(n):
    # return a list of fibonacci numbers
    fibonacci_list= [0,1] ## The Fibonacci sequence starts with: 0, 1
    if n == 0:
        return []
    elif n == 1:
        return [0]
    for i in range(2,n):
        sum_of_2_num=fibonacci_list[i-2]+fibonacci_list[i-1] ## Each new number is the sum of the two preceding numbers.
        fibonacci_list.append(sum_of_2_num)
    return fibonacci_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

