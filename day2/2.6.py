day_of_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day, month, year):
    allday = 0
    if is_leap(year):
        day_of_month[2] += 1
    else:
        if month == 2 and day == 29:
            return -1
    for i in range(1,month):
        allday += day_of_month[i]
    allday += day

    return allday

# d, m ,y = input("input : ").split()
# print(day_of_year(int(d),int(m),int(y)))
print(day_of_year(1,1,1999))

    