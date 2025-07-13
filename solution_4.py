# Task: Given a string s and an integer k (where len(s) is divisible by k),
# split s into len(s)/k substrings of length k.
# For each substring, remove duplicate characters while preserving order,
# and print the result on separate lines.

# Example:
# Input:  s = "AABCAAADA", k = 3
# Substrings: ["AAB", "CAA", "ADA"]
# Output: 
# AB
# CA
# AD



def merge_tools(string,k):
    for i in range(0,len(string), k): ## i=o,k,2K,3K,...,len(string)-1
        
        sub_string=string[i:i+k]  ## sub_string=string[0:k], string[k:2k], ......
        
        no_duplicates = ""
        for char in sub_string:
            
            if char not in no_duplicates: ## check if char is not in no_duplicates
                no_duplicates += char    ## add char to no_duplicates if not already present
        
        print(no_duplicates)


# Example usage
if __name__ == "__main__":
    merge_tools("AABCAAADA", 3)
    
    # output:
    # AB
    # CA
    # AD
