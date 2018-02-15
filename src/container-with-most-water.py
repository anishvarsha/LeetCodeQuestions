import math

a = list(map(int, raw_input().split(" ")))

n = len(a)
b = []
b.extend(range(1, n+1))
great = 0

for i in range(len(a)):
	sumVal = a[i]**2+b[i]**2
	area = (0.5)*(math.sqrt(sumVal))**2
	print area
