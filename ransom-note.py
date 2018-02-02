r = list("aa")
m = list("aab")

rDic = {}
mDic = {} 

for i in r:
    if i not in rDic:
        rDic[i] = 1
    else:
        rDic[i]+=1

for i in m:
    if i not in mDic:
        mDic[i] = 1
    else:
        mDic[i]+=1
print mDic
print rDic
if len(rDic.keys()) > len(mDic.keys()):
    print "1"
    print False
for i in rDic.keys():
    if i not in mDic.keys():
        print i
        print False
    if rDic[i] > mDic[i]:
        print mDic[i]
        print rDic[i]
        print False
print True