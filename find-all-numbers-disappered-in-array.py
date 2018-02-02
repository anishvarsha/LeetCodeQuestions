nums = map(int, raw_input().split(" "))
nums.sort()
n = nums[-1]
sumVals = n*(n+1)/2
sumList = sum(nums)
print sumVals-sumList	