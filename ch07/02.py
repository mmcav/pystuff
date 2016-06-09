def evensum(inputlist):
    count = 0
    for i in inputlist:
        if i % 2 == 0:
            count += i
    return count

test1 = [2, 4, 5, 1, 0, -2, 7, 10, 3]
output = evensum(test1)
print(output)
print(2+4+0-2+10)
