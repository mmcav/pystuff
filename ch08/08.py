def reverse(string):
    count = len(string)
    newstr = ""
    while count > 0:
        newstr += string[count-1]
        count -= 1
    return newstr

def mirror(string):
    mirrorstr = reverse(string)
    newstr = string + mirrorstr
    return newstr


print(mirror("good") == "gooddoog")
print(mirror("Python") == "PythonnohtyP")
print(mirror("") == "")
print(mirror("a") == "aa")
