a = map(int,raw_input().split(" "))
j = list()
k = 0
for i in range(0, len(nums)):
	if a[i] != 1:
		j.append(k)
		k = 0
	else:
		k+=1
j.append(k)
print max(j)
