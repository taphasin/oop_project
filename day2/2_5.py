def only_english(string1):
    l = [i for i in string1 if i > 'a' and i < 'z']
    x = ''
    return x.join(l)
x = "w6fewko546568"
print(only_english(x))