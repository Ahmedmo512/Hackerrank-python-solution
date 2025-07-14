# Task:
# Given integers x, y, z, and n, generate a list of all possible 3D coordinates (i, j, k)
# such that 0 <= i <= x, 0 <= j <= y, 0 <= k <= z, and the sum i + j + k != n.
# Use list comprehension and output the resulting list in lexicographic order.

# Input Format:
# Four lines of input, each containing an integer: x, y, z, n

#  Output Format:
# Print the list of valid coordinates.


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
