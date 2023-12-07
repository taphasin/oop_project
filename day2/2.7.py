day_of_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_of_year(day, month, year):
    day_of_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
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



def day_in_year(year):
    if is_leap(year):
        return "366"
    else:
        return "365"

def date_diff(date1, date2):
    spfir = date1.split("-")
    spsec = date2.split("-")

    infir = [eval(i) for i in spfir]
    insec = [eval(i) for i in spsec]
    if insec[1] > 12 or insec[1] < 1 or infir[1] > 12 or infir[1] < 1:
        return -1

    if is_leap(infir[2]):
        day_of_month[2] = 29
    else:
        day_of_month[2] = 28
    if infir[0] > day_of_month[infir[1]] or infir[0] < 1:
        return -1


    if is_leap(insec[2]):
        day_of_month[2] = 29
    else:
        day_of_month[2] = 28
    if insec[0] > day_of_month[insec[1]] or infir[0] < 1:
        return -1


    sum1 = day_of_year(infir[0], infir[1], infir[2])
    sum2 = day_of_year(insec[0], insec[1], insec[2])

    sumyer = (insec[2] - infir[2] - 1) * 365
    if is_leap(infir[2]):
        fy = 366
    else:
        fy = 365
        
    sumall = (fy - sum1) + sum2 + sumyer + 1

    for a in range(infir[2],insec[2]):
        if is_leap(a):
            sumall += 1

    return sumall

print(date_diff("25-12-1999", "9-13-2000"))