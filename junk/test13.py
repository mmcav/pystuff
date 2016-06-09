def listodd(listtest):
    count = 0
    for i in listtest:
        if i % 2 == 1:
            count += 1
    return count

#listtest = (1,2,3,4,5,6,7,8,9)
count = listodd((1,2,3,4,5,6,7,8,9))
print("The list has {0} odd numbers.".format(count))
