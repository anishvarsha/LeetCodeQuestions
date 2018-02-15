nums = raw_input().split(",")

d = {}
l = []
for i in nums:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i]+=1
        
for i in d.keys():
    if d[i]==2:
        l.append(i)
print l