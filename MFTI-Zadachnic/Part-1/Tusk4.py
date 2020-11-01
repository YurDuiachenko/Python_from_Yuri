from math import sqrt
l = [i  for i in range(2500) if i%10 == 1 and sqrt(i)%1 == 0]
print(l)