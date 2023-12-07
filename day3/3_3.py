def is_plusone_dictionary(d):
  c = 0
  for (i,a) in d.items():
    print(a,c,i)
    if a - i != 1 or i - c != 1:
      return False
    c = a
  return True
 
x = {1:2, 3:4, 5:6, 8:9}
print(is_plusone_dictionary(x))