def is_prime(n):
    if n <= 3:
        return (n == 2 or n == 3)
    else:
        limit = int(n**0.5)
        for i in range(2, limit+1): #up to sqrt(n), based on the primality test
            if n % i == 0:
                return False
        return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))
print(is_prime(10))
print(is_prime(11))
##print(is_prime(35))
##print(is_prime(19911122))
##print(is_prime(19911121)) #large prime number
##print(is_prime(9996000319)) #non prime, composed by two large primes
