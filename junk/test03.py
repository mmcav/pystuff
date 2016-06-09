p = 10000
n = 12
r = 0.08
t = input("Number of years 't': ")
tt = float(t)
a = p*(1+r/n)**(n*tt)
print("Result:",a)
print("debug:",type(t))

