a = list(map(int, raw_input().split(" ")))

l = len(a)

for i in range(0, l-1):
	print i
	if a[i]>=a[i+1]:
		print str(a[i])+","+str(a[i+1])
