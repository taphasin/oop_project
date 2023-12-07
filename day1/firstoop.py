sh, sm, eh, em = input().split()
sum = ((int(eh)*60) + int(em)) - ((int(sh)*60) + int(sm))

if sum <= 15:
    print(0)
    quit()

sum = sum / 60
if sum % 1 > 0:
    sum += 1

sum = int(sum)

if 1 <= sum < 4:
    print(sum*10)

elif 4 <= sum < 6:
    print((sum*20)-30)

elif sum >= 6:
    print((int(sum/24)+1)*200)