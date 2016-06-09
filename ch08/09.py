def remove_letter(char, string):
    newstr = ""
    for i in string:
        if i != char:
            newstr += i
    return newstr

print(remove_letter("a", "apple") == "pple")
print(remove_letter("a", "banana") == "bnn")
print(remove_letter("z", "banana") == "banana")
print(remove_letter("i", "Mississippi") == "Msssspp")
print(remove_letter("b", "") == "")
print(remove_letter("b", "c") == "c")
