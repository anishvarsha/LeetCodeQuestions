nums = map(int, raw_input().split(","))

for i in range(len(nums)-1):
	if abs(nums[i]-nums[i+1]) >=2:
		return (nums[i]+nums[i+1])/2