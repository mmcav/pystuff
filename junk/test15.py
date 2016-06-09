a = [5, 6, 7, 8, 9]
b = a
c = [[], [], [], [], []]

for i in (range(len(a))):
    c[i] = a[i]
##c = a

print(a)
print(b)
print(c)
print(a is b)
print(a is c)
print(b is c)

a[0] = 10

print(a)
print(b)
print(c)
