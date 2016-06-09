def remove_all(substr, string):
    newstr = ""
    lensub = len(substr)
    lenstr = len(string)
    count = 0
    while count < lenstr:
        if substr != string[count:count+lensub]:
            newstr += string[count]
            count += 1
        else:
            count += lensub
    return newstr

print(remove_all("an", "banana"))
print(remove_all("cyc", "bicycle"))
print(remove_all("iss", "Mississippi"))
print(remove_all("eggs", "bicycle"))
