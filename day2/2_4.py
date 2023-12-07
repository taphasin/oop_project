'''
def count_minus(str):
  ft = [for i in str if i > 0]
  return ft

st = input("input ")
st = st.split(" ")
st = [eval(i) for i in st]
print(count_minus(st))

'''

def count_minus(str):
    x = str.split(" ")
    y = [i for i in x if int(i) > 0]
    return len(y)

x = "1 2 3 4 5"
print(count_minus(x))