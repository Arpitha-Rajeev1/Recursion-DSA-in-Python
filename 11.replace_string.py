def replace(s,o,r):
    if len(s) == 0:
        return s
    if s[0] == o:
        return r + replace(s[1:],o,r)
    return s[0] + replace(s[1:],o,r)

print(replace('dacdxcd', 'c', 'x'))
