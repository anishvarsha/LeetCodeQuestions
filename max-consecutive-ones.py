class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        count = 0
        for i in nums:
            if i == 0:
                l.append(count)
                count = 0
            else:
                count+=1
        l.append(count)
        return max(l)