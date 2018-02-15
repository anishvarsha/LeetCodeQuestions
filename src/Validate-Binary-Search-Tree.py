# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
INT_MAX = 4294967296
INT_MIN = -4294967296
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.bst(root, INT_MIN, INT_MAX)
    
    def bst(self, node, minVal, maxVal):
        if node is None:
            return True
        if node.val<minVal or node.val >maxVal:
            return False
        return self.bst(node.left, minVal, node.val-1) and self.bst(node.right, node.val+1, maxVal)
            