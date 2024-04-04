# Suppose you have a string, S, made up of only 'a's and 'b's.
# Write a recursive function that checks if the string was generated using the
# following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise
# return false.

def checkab(s):
    if len(s) == 0:
        return True
    if s[0] == 'a':
        if len(s) == 1:
            return True
        elif s[1] == 'a':
            return checkab(s[1:])
        elif len(s) >= 3 and s[1] == 'b' and s[2] == 'b':
            return checkab(s[2:])
        else:
            return False
    elif s[0] == 'b':
        if len(s) == 1:
            return True
        elif s[1] == 'a':
            return checkab(s[1:])
        else:
            return False


def check(s):
    if s[0] != 'a':
        return False
    return checkab(s)


s = input()
if check(s):
    print('true')
else:
    print('false')
