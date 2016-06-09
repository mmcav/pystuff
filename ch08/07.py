def reverse(string):
    count = len(string)
    newstr = ""
    while count > 0:
        newstr += string[count-1]
        count -= 1
    return newstr

print(reverse("happy") == "yppah")
print(reverse("Python") == "nohtyP")
print(reverse("") == "")
print(reverse("a") == "a")
