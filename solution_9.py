# Task:
# - Filter a list of email addresses, keeping only the valid ones.
# - A valid email must follow the pattern:
#     username@websitename.extension
#     - username: can contain letters, digits, dashes (-), underscores (_)
#     - websitename: only letters and digits
#     - extension: only letters, max 3 characters
# - Use filter() and lambda or regex to validate each email.
# - Return the valid emails sorted lexicographically.

# Example:
# Input: ['lara@hackerrank.com', 'brian-23@hackerrank.com', 'britts_54@hackerrank.com']
# Output: ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']


def fun(email):
    # return True if s is a valid email, else return False

    if '@' not in email or '.' not in email:
        return False

    try:
        username, rest = email.split('@')
        website, extension = rest.split('.')
    except ValueError:
        return False

   
    if not username.replace('-', '').replace('_', '').isalnum():
        return False
    if not website.isalnum():
        return False
    if not (extension.isalpha() and len(extension) <= 3):
        return False

    return True

def filter_mail(emails):
    valid = []
    for email in emails:
        if fun(email):
            valid.append(email)
    return valid


if __name__ == '__main__':
    n = int(input())
    emails = [input() for _ in range(n)]
    valid_emails = filter_mail(emails)
    print(sorted(valid_emails))

