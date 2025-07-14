# Task:
# Given integers x, y, z, and n, generate all possible 3D coordinates [i, j, k]
# such that 0 <= i <= x, 0 <= j <= y, 0 <= k <= z and i + j + k != n.
# This challenge helps practice list comprehensions and conditional filtering in Python.

# Input:
# - 4 integers: x, y, z, n

# Output:
# - A list of all valid coordinate lists [i, j, k] sorted in lexicographic order.


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    


coordinates = [[i, j, k]
               for i in range(x + 1)
               for j in range(y + 1)
               for k in range(z + 1)
               if i + j + k != n]

print(coordinates)


# Example:
# Input:
# 1
# 1
# 1
# 2
# Output:
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
