s = list(raw_input())
k = int(raw_input())

newList = []
n = len(s)


for i in range(k):
	if i<=n-1:
		newList.append(s[i])

print newList[::-1]+s[k:]
