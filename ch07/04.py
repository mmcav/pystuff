def len5count(inputlist):
    count = 0
    for i in inputlist:
        if isinstance(i, str):
            if len(i) == 5:
                count += 1
    return count

test1 = ("lalala", "okla", "okoko", "word", "worlds", "words", 12345, "hmmm?")
print(len5count(test1))
