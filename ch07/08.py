def print_multiples(n, high):
    for i in range(1, high+1):
        if n*i < 10:
            print(n * i, end="   ")
        else:
            print(n * i, end="  ")
    print()

def print_mult_table(high):
    for i in range(1, high+1):
        print_multiples(i, high)

print_mult_table(7)
