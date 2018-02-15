# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.toBst(nums, 0, len(nums))
    
    def toBst(self, nums, left, right):
        if left ==  right:
            return None
        
        mid = (left+right)>>1
        root = TreeNode(nums[mid])
        root.left = self.toBst(nums, left, mid)
        root.right = self.toBst(nums, mid+1, right)
        
        return root