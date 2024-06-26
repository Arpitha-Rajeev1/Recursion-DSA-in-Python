# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    if len(string) == 0 or len(string) == 1:
        return string
    if string[0] == string[1]:
        return removeConsecutiveDuplicates(string[1:])
    return string[0] + removeConsecutiveDuplicates(string[1:])


# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
