class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        mapper = {}
        for i in range(1, len(nums)+1):
            if i in mapper:
                pass
            else:
                mapper[i] = 0
            
            if nums[i-1] in mapper:
                mapper[nums[i-1]]+=1
            else:
                mapper[nums[i-1]] = 1
        for k, v in mapper.iteritems():
            if v == 0:
                ret.append(k)
        return ret