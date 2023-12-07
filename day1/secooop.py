first  = 999
second = 999
num = ' '
while first > 100:
    second = 999
    while second > 100:
        sum = str(first * second)
        if sum > num:
            pal = sum [::-1]
            if pal == sum:
                num = sum
            second -= 1
    first -= 1

print(num)
