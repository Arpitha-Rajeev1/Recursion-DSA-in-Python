def replacePi(string): 
    if len(string) == 0 or len(string) == 1:
        return string
    if string[0] == 'p' and string[1] == 'i':
        return '3.14' + replacePi(string[2:])
    return string[0] + replacePi(string[1:])

# Main
string = input()
print(replacePi(string))
