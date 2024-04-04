def convert(s):
    print(s)
    if len(s) == 1:
        return ord(s) - 48
    return convert(s[0]) * 10**(len(s)-1) + convert(s[1:])


s = input()
print(convert(s))
