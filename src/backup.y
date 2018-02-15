class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
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
                        end = j
                        break
                if count>0:
                    break
            k = nums[begin+1:]
            k.sort()
            j = nums[:begin+1]
            nums = j+k
        if count == 0:
            nums.sort()

def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    return [int(number) for number in input.split(",")]

def integerListToString(nums, len_of_list=None):
    result = ""
    if not len_of_list:
        len_of_list = len(nums)
    for index in range(len_of_list):
        num = nums[index]
        result += str(num) + ", "
    return result[:-2]

import sys
def readlines():
    for line in sys.stdin:
        yield line.strip('\n')

def main():
    nums = raw_input().strip(" ")
    nums = map(int, nums)
    ret = Solution().nextPermutation(nums)
    print nums

if __name__ == '__main__':
    main()