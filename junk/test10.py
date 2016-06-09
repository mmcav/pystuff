##def bad_absolute_value(x):
##    if x < 0:
##        return -x
##    elif x > 0:
##        return x
##
##a = bad_absolute_value(0)
##print(type(a))

##a = int(input("1: "))
##b = int(input("2: "))
##
##if (a % b == 0) == False:
##    print("okay")
##else:
##    print("not okay")

##def absolute_value(n):   # Buggy version
##    if n < 0:
##        return -n
##    elif n > 0:
##        return n

##def test_suite():
##    test(absolute_value(17) == 17)
##    test(absolute_value(-17) == 17)
##    test(absolute_value(0) == 0)
##    test(absolute_value(3.14) == 3.14)
##    test(absolute_value(-3.14) == 3.14)

##test_suite()

##def clockwise(di):
##    if di == "N":
##        return "E"
##    if di == "E":
##        return "S"
##    if di == "S":
##        return "W"
##    if di == "W":
##        return "N"
##
##test(clockwise("N") == "E")
##test(clockwise("W") == "N")
##test(clockwise(42) == None)

##test(dayname(3) == "Wednesday")
##test(dayname(6) == "Saturday")
##test(dayname(42) == None)
##test(dayname(-1) == None)
##test(daynum("Friday") == 5)
##test(daynum("Sunday") == 0)
##test(daynum(dayname(3)) == 3)
##test(dayname(daynum("Thursday")) == "Thursday")
##test(daynum("Halloween") == None)

##test(dayadd("Monday", 4) ==  "Friday")
##test(dayadd("Tuesday", 0) == "Tuesday")
##test(dayadd("Tuesday", 14) == "Tuesday")
##test(dayadd("Sunday", 100) == "Tuesday")
##test(dayadd("Sunday", -1) == "Saturday")
##test(dayadd("Sunday", -7) == "Sunday")
##test(dayadd("Tuesday", -100) == "Sunday")

##test(tosecs(2, 30, 10) == 9010)
##test(tosecs(2, 0, 0) == 7200)
##test(tosecs(0, 2, 0) == 120)
##test(tosecs(0, 0, 42) == 42)
##test(tosecs(0, -10, 10) == -590)
##test(tosecs(2.5, 0, 10.71) == 9010)
##test(tosecs(2.433,0,0) == 8758)

##test(hoursin(9010) == 2)
##test(minutesin(9010) == 30)
##test(secondsin(9010) == 10)

##test(intercept(1, 6, 3, 12) == 3.0)
##test(intercept(6, 1, 1, 6) == 7.0)
##test(intercept(4, 6, 12, 8) == 5.0)

##test(is_factor(3, 12))
##test(not is_factor(5, 12))
##test(is_factor(7, 14))
##test(not is_factor(7, 15))
##test(is_factor(1, 15))
##test(is_factor(15, 15))
##test(not is_factor(25, 15))


import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def dayname(n):
    """ Hi """
    week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    if n >= 0 and n <= 6:
        return week[n]

def daynum(string):
    """ Hello """
    if string == "Sunday":
        return 0
    if string == "Monday":
        return 1
    if string == "Tuesday":
        return 2
    if string == "Wednesday":
        return 3
    if string == "Thursday":
        return 4
    if string == "Friday":
        return 5
    if string == "Saturday":
        return 6

def dayadd(string, n):
    n1 = daynum(string)
    n2 = (n1 + n) % 7
    print(n1 + n)
    n3 = dayname(n2)
    return n3

def tosecs(hr, mn, secs):
    a_secs = (hr*60 + mn)*60 + secs
    return int(a_secs)

def hoursin(secs):
    h = secs/3600
    return int(h)

def minutesin(secs):
    mn = (secs/60) % 60
    return int(mn)

def secondsin(secs):
    s = secs % 60
    return s

def slope(x1, y1, x2, y2):
    tg = abs(y1 - y2)/abs(x2 - x1)
    return tg

def intercept(x1, y1, x2, y2):
    tg = slope(x1, y1, x2, y2)
    if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
        yi = y1-tg*x1
    else:
        yi = tg*x1+y1
    return yi

def is_factor(f, n):
    return n % f == 0

def f2c(t):
    return round((t-32)/1.8)

def c2f(t):
    return round(1.8*t+32)

test(f2c(212) == 100)     # Boiling point of water
test(f2c(32) == 0)        # Freezing point of water
test(f2c(-40) == -40)     # Wow, what an interesting case!
test(f2c(36) == 2)
test(f2c(37) == 3)
test(f2c(38) == 3)
test(f2c(39) == 4)

test(c2f(0) == 32)
test(c2f(100) == 212)
test(c2f(-40) == -40)
test(c2f(12) == 54)
test(c2f(18) == 64)
test(c2f(-48) == -54)
