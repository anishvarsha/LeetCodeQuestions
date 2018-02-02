nums = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 2], [3, 4], [5, 6], [7, 8]]

b = []

r = int(raw_input())
c = int(raw_input())

if r*c != len(nums[0])*len(nums):
	print nums

for i in nums:
	for j in  i:
		b.append(j)

d = [[] for _ in range(r)]
print d
k = 0
for i in range(r):
	for j in range(c):
		d[k].append(b[0])
		b.remove(b[0])
	k+=1
print d