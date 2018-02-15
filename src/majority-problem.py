dic = {}
nums = [1,1,2,2,2]
for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i]+=1
print dic
l = len(nums)
for i in dic.keys():
    if dic[i]>l/2:
        print i
