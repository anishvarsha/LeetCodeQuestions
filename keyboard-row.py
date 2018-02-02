rowOne = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
rowTwo = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
rowThree = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

words = raw_input().split(" ")
arr = list()
for i in words:
	k = list(i)
	j = [item.lower() for item in k]
	if set(j) & set(rowOne) == set(j):
		p = "".join(k)
		arr.append(p)
	if set(j) & set(rowTwo) == set(j):
		p = "".join(k)
		arr.append(p)
	if set(j) & set(rowThree) == set(j):
		p = "".join(k)
		arr.append(p)
print arr