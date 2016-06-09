print("{0:>2} ".format(""), end="  ")
for i in range(1, 13):
    print("{0:>4}".format(i), end="")
print("\n  :--------------------------------------------------")
for i in range(1, 13):
    for j in range(1, 13):
        if j == 1:
            print("{0:>2}:".format(i), end="  ")
        print("{0:>4}".format(i*j), end="")
    print("\n", end="")
