def sumuptoeven(inputlist):
    count = 0
    for i in inputlist:
        if i % 2 != 0:
            count += i
        else:
            break
    return count

test1 = (1, 3, 5, 7, 9, 10)
test2 = (2, 3, 4, 5, 6, 7)
test3 = (1, -3, 5, -7, 9, -11, -2, -1, 4)
test4 = (1, 3, 5, 7, 9, 11)
print(sumuptoeven(test1))
print(sumuptoeven(test2))
print(sumuptoeven(test3))
print(sumuptoeven(test4))
