nums = map(int, raw_input().split(","))

dic = {}
for i in range(len(nums)):
	if dic.has_key(nums[i]):
		dic[nums[i]]+=1
	else:
		dic[nums[i]] = 1

print dic
dicNew = sorted(dic.items(), key = lambda x:x[1])
print dicNew
if dicNew[0][1] <2:
	print dicNew[0][0]
else dicNew[len(dicNew)-1]>2:
	print dicNew[len(dicNew)-1][0]

#17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6