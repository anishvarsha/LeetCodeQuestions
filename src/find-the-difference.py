a = list(raw_input())
b = list(raw_input())


a.sort()
b.sort()
for i in range(len(b)-1):
	if a[i]!=b[i]:
		print b[i]
print b[len(b)-1]