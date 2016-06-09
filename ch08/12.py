def remove(substr, string):
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
            break
    for i in range(count, lenstr):
        newstr += string[i]
    return newstr

print(remove("an", "banana"))
print(remove("cyc", "bicycle"))
print(remove("iss", "Mississippi"))
print(remove("eggs", "bicycle"))
