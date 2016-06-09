def negsum(inputlist):
    count = 0
    for i in inputlist:
        if i < 0:
            count += i
    return count


test1 = (1, 2, 3, 4, 5, -1, -2, 6, 0, -50)
test2 = (0, 1, 10, 3, -1.3, 2.45, -0.6, 0.0000011)
print(negsum(test1))
print(negsum(test2))
