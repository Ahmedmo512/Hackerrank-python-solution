# Given an array of integers and two sets A (liked) and B (disliked),
# compute the happiness score: +1 for each element in A, -1 for each in B.
# Output the final happiness score after processing the array.



n,m=list(map(int,input().split()))
array=list(map(int,input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

count=0

for i in range(n):
    if array[i] in A:
        count+=1
    elif array[i]  in B :
        count -=1
    else:
        count+=0

print(count)      
