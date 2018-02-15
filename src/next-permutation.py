nums = map(int, list(raw_input()))
nums = list(nums)
print nums
count = 0
begin = 0
end = 0
if len(nums) == 0 or len(nums)==1:
    print

else:
    for i in reversed(range(0, len(nums))):
        for j in reversed(range(0, i)):
            if nums[i] > nums[j]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                count+=1
                begin = j
                break
        if count>0:
            break
    k = nums[begin+1:]
    k.sort()
    j = nums[:begin+1]
    nums = j+k
if count == 0:
    nums.sort()
print nums