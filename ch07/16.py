def sum_of_squares(inputlist):
    count = 0
    for i in inputlist:
        count += i**2
    return count

print(sum_of_squares([2, 3, 4]) == 29)
print(sum_of_squares([ ]) == 0)
print(sum_of_squares([2, -3, 4]) == 29)
