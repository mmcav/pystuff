def num_digits(n):
    count = 0
    if n < 0:
        n = abs(n)
    while True:
        count = count + 1
        n = n // 10
        if n == 0:
            break
    return count

print(num_digits(0))
