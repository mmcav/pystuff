def replace(s, old, new):
    lgth = len(old)
    templist = list(s)
    tempold = list(old)
    tempnew = list(new)
    for i in range(len(templist)):
        if templist[i:i+lgth] == tempold:
            templist[i:i+lgth] = tempnew
    newstr = "".join(templist)
    return newstr


print(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

print(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
