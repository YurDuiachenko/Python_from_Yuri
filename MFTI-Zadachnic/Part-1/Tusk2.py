a = input().split()
l = len(a)
for i in range(l):
	a[i] = int(a[i])
for i in range(l):
    for j in range(0, l-i-1):
    	if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)