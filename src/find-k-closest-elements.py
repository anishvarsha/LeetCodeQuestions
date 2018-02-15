a = map(int, raw_input().split(" "))
k = int(raw_input())
x = int(raw_input())

index = 0
dic = []


	for i in range(len(a)):
		dic.append((a[i], a[i]-x))

final = []
sortedDic = sorted(dic, key = lambda x:x[1])
print sortedDic

for i in range(k):
	final.append(sortedDic[i][0])

print final