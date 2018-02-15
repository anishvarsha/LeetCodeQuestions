n = int(raw_input().strip(" "))
final = []
a = [1]
b = [1, 1]

if n == 1:
	final.append(a)
elif n == 2:
	final.append(a)
	final.append(b)
else:
	final.append(a)
	final.append(b)
	for i in range(2, n):
		k = final[i-1]
		a = [1]
		for i in range(len(k)-1):
			su = k[i]+k[i+1]
			a.append(su)
		a.append(1)
		final.append(a)

print final

