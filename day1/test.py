num = 0
for i in range(999, 100, -1):
    for b in range(999, 100, -1):
        x = i * b
        if x > num:
            s = str(i * b)
            p = s[::-1]
            if s == p:
                num = i * b

print(num)