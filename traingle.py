triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]]
for i in triangle:
            i.sort()
su = 0
for i in triangle:
    su+=i[0]
print su