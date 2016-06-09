def tri_test(a, b, c):
    if c >= b and c >= a:
        hyp = c
        cat1 = a
        cat2 = b
    else:
        if b >= a:
            hyp = b
            cat1 = a
            cat2 = c
        else:
            hyp = a
            cat1 = b
            cat2 = c
    if abs(hyp - (cat1**2 + cat2**2)**0.5) < 0.0000001:
        return True
    else:
        return False

a = float(input("First side of triangle: "))
b = float(input("Second side of triangle: "))
c = float(input("Third side of triangle: "))

if tri_test(a,b,c) == True:
    print("Right-angled.")
else:
    print("Not right-angled.")
