x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ]

def delete_minus(x):
    sumlist = [ [list[y] for y in range(len(list)) if list[y] >= 0] for list in x]
    return sumlist

print(delete_minus(x))