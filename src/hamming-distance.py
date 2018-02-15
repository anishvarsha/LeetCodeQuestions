(x, y) = map(int, raw_input().split(' '))
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

def lenBin(arr, lenArr, lenToArr):
	diff = lenToArr - lenArr
	for i in range(0, diff):
		arr.append(0)
	return arr

def findDiff(x, y):
	k = [i for i, j in zip(x, y) if i != j]
	return k

binX = binaryMethod(x)
binY = binaryMethod(y)

print binX
print binY

lenBinX = len(binX)
lenBinY = len(binY)
count = 0
if lenBinX < lenBinY:
	binX = lenBin(binX, lenBinX, lenBinY)
	binX = binX[::-1]
	binY = binY[::-1]
	count = findDiff(binX, binY)

elif lenBinX > lenBinY:
	binY = lenBin(binY, lenBinY, lenBinX)
	binY = binY[::-1]
	binX = binX[::-1]
	count = findDiff(binX, binY)

elif lenBinX == lenBinY:
	count = findDiff(binX, binY)
print binX
print binY
print len(count)