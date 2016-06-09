def oddcount(listinput):
    count = 0
    for i in listinput:
        if i % 2 != 0:
            count += 1
    return count

test1 = [2, 3, 4, 5, 6, 7, 8, -1]
output = oddcount(test1)
print(output)
