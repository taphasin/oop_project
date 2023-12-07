ls = input().split()
ls.sort()

while ls[0] == '0':
    ls.insert(0,ls[1])
    ls.pop(2)



for i in ls:
    print(i, end="")