def num_digits(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count

print(num_digits(0) == 1)
