s = list(raw_input().strip())

vowels = ['a', 'e', 'i', 'o', 'u']
n = len(s)
newList = []

for i in s:
	if i in vowels:
		newList.append(i)

newList = newList[::-1]

j = 0
for i in range(n):
	if s[i] in vowels:
		s[i] = newList[j]
		j+=1
print ''.join(s)