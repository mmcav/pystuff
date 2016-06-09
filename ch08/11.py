def count(substr, string):
    count = 0
    lensub = len(substr)
    lenstr = len(string)
    if lenstr >= lensub:
        diff = lenstr - lensub
        for i in range(diff+1):
            if substr == string[i:i+lensub]:
                count += 1
    return count

print(count("is", "Mississippi"))
print(count("an", "banana"))
print(count("ana", "banana"))
print(count("nana", "banana"))
print(count("nanan", "banana"))
print(count("aaa", "aaaaaa"))
print(count("apple", "apple"))
