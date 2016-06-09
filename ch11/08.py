def cross_product(u, v):
    if len(u) == len(v) and len(u) == 3:
#        vcross = [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
        ab = ((1, 2), (2, 0), (0, 1))
        vcross = []
        for (i, j) in ab:
            vcross.append(u[i]*v[j]-u[j]*v[i])
        return vcross


print(cross_product([2, 3, 4], [5, 6, 7]) == [-3, 6, -3])
