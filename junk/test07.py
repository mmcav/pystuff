def weekday(n):
    if n == 0:
        day = "Sunday."
    elif n == 1:
        day = "Monday."
    elif n == 2:
        day = "Tuesday."
    elif n == 3:
        day = "Wednesday."
    elif n == 4:
        day = "Thursday."
    elif n == 5:
        day = "Friday."
    elif n == 6:
        day = "Saturday."
    else:
        day = "Error. Invalid input."
    return day

#n = int(input("What is the number of the week? "))
first = int(input("Starting day? "))
length = int(input("How long? "))
#n = (length % 7) + (first % 7)
n = (first + length) % 7
ans = weekday(n)
print("The day in question is a... ", ans)
