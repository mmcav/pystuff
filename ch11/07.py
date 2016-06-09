def dot_product(u, v):
    if len(u) == len(v):
        vdot = 0
        for i in range(len(u)):
            vdot += u[i]*v[i]
        return vdot

print(dot_product([1, 1], [1, 1]) ==  2)
print(dot_product([1, 2], [1, 4]) ==  9)
print(dot_product([1, 2, 1], [1, 4, 3]) == 12)
