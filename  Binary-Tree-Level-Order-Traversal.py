# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        traverseList, level = [], [root]
        while root and level:
            currentNodes = []
            nextNodes = []
            for node in level:
                currentNodes.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            level = nextNodes
            traverseList.append(currentNodes)
        return traverseList