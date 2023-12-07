def char_count(str):
    dic = {}
    for i in str:
        dic[i] = str.count(i) 
    return dic
    
print(char_count("hello world"))

