def num_even_digits(n):
    count = 0
    if n < 0:
        n = abs(n)
    while True:
        if n % 2 == 0:
            count += 1
        n = n // 10
        if n == 0:
            break
    return count

print(num_even_digits(123456) == 3)
print(num_even_digits(2468) == 4)
print(num_even_digits(1357) == 0)
print(num_even_digits(0) == 1)
