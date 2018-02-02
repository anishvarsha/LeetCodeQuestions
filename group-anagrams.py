a = list(raw_input().split(" "))

print a
b = list()
count = 0

for i in range(len(a)):
	 k = sorted(list(a[i]))
	 if k not in b:
	 	b.append(k)
n = len(b)

x = [[] for i in range(n)]

for i in range(len(a)):
	if sorted(list(a[i])) in b: