a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print a[::-1]
count = 0
k = len(a)
l = 0
for i in range(len(a)):
	j = i
	while j<len(a):
		temp = a[i][j]
		a[i][j] = a[j][i]
		a[j][i] = temp
		count+=1
		j+=1
print a
