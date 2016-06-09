def wordcountsam(inputlist):
    count = 0
    for i in inputlist:
        count += 1
        if i == "sam":
            break
    return count

test1 = ("max", "names", "whatevs", "y?", "sam")
test2 = ("same", "thing", "all", "over", "again")
test3 = ("sam", "and", "max")
test4 = ("last test", "sam")
print(wordcountsam(test1))
print(wordcountsam(test2))
print(wordcountsam(test3))
print(wordcountsam(test4))
