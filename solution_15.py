# Task:
# Given two sets of student roll numbers:
#   - One for students subscribed to the English newspaper
#   - One for students subscribed to the French newspaper
# Your task is to compute the number of students who have subscribed to
# either the English or the French newspaper, but not both.

# Input:
# - First line: Number of students subscribed to English
# - Second line: Space-separated list of roll numbers for English subscribers
# - Third line: Number of students subscribed to French
# - Fourth line: Space-separated list of roll numbers for French subscribers

# Output:
# - A single integer: total number of students subscribed to only one newspaper


english_count = int(input())
english_set = set(map(int, input().split()))

french_count = int(input())
french_set = set(map(int, input().split()))

result = english_set.symmetric_difference(french_set)

print(len(result))
