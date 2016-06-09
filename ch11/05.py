def add_vectors(u, v):
    if len(u) == len(v):
        vsum = []
        for i in range(len(u)):
            vsum.append(u[i] + v[i])
        return vsum

print(add_vectors([1, 1], [1, 1]) == [2, 2])
print(add_vectors([1, 2], [1, 4]) == [2, 6])
print(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
