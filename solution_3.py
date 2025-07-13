# Task: Manually convert lowercase to uppercase and vice versa in a string.
# Avoid using str.swapcase(). Use character-by-character checks instead.

## Sample Input 0                        ------>>  Sample Output 0 

## HackerRank.com presents "Pythonist 2"  ---->>       hACKERrANK.COM PRESENTS "pYTHONIST 2"


def creat_swap_case_function(s):
    
    result=""
    
    for i in range (len(s)):
       
        if s[i].islower():
            result=result+s[i].upper()
       
        elif s[i].isupper():
            result=result+s[i].lower()
       
        else:
            result=result+s[i]
    
    return result
