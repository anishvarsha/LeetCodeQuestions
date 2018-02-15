nums = list(map(int, raw_input().split(" ")))
target = int(raw_input().strip(" "))

index = 0
prev = 0
for i in range(len(nums)):
	if nums[i] == target:
		index = i
length = len(nums)
if target<nums[0]:
	index = 0
elif nums[length-1]<target:
	index = length
if index == 0:
	for i in range(length-1):
		if nums[i+1]>target and nums[i]<target:
			index = i+1
		
print index