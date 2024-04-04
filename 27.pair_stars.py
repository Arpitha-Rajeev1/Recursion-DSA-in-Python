def star(s):
    if len(s) == 1:
        return s
    if s[0] == s[1]:
        return s[0] + '*' + star(s[1:])
    return s[0] + star(s[1:])


s = input()
print(star(s))
