s = "leetcode"
s = list(s)
listS = []
for i in range(len(s)):
	if s[i] not in listS:
		listS.append([s[i], 1])

