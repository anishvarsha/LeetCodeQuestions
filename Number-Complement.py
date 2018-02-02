def binaryMethod(a):
	arr = list()
	if a == 0:
		arr.append(0)
		return arr
	elif a == 1:
		arr.append(1)
		return arr
	else:
		while a!=0:
			arr.append(a%2)
			a = a/2
	return arr

num = int(raw_input())

binX = binaryMethod(num)
binX = binX[::-1]	
print binX
binX = [1 if i == 0 else 0 for i in binX]
print binX
n = len(binX)-1
a = 0
for i in binX:
	#print a
	a += 2**n*i
	#print "after: "+str(a)
	n = n-1
print a