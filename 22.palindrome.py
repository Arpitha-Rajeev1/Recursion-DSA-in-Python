def palindrome(s, si, ei):
    if si >= ei:
        return True
    if s[si] == s[ei]:
        return palindrome(s, si+1, ei-1)
    else:
        return False

s = input()
if palindrome(s, 0, len(s)-1):
    print('true')
else:
    print('false')

