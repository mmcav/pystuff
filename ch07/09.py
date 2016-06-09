def print_triangular_numbers(n):
    count = 0
    for i in range(1, n+1):
        count += i
        print(i, "\t", count)

print_triangular_numbers(20)
