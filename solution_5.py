# Task: Manually check if a given string contains:
# - Alphanumeric, alphabetical, digit, lowercase, and uppercase characters.




if __name__ == '__main__':
    s = input()

    
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    for char in s:
        if char.isalnum():
            has_alnum = True
        if char.isalpha():
            has_alpha = True
        if char.isdigit():
            has_digit = True
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)


#### Another solution 


if __name__ == '__main__':
    s = input()

    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
