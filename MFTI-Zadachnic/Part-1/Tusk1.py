#������������� �������
def summ(a):
	sum1 = 0
	for i in a:
		sum1 = sum1 + i
	return sum1
	
#�������� �������
#��������
def maxi(a):	
	m = 0
	for i in range(len(a)):
		if a[i] >= m :
			m = a[i]
	return m

#�������
def mini(a):
	m = maxi(a)
	for i in range(len(a)):
		if a[i] <= m :
			m = a[i]
	return m

#������� ��������������
def average(a):
	sum1 = summ(a)
	return sum1//len(a)

#������� ����������
def o(a):
	av = average(a)
	l = []*len(a)
	for i in range(len(a)):
		l.append((a[i]-av)*(a[i]-av))
	s = summ(l)/len(a)
	return s
		
t = input().split()
for i in range(len(t)):
	t[i] = int(t[i])
#������ ������ �������, ������� ������ ���������, �������� - maxi
print(maxi(t))