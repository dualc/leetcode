# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root and root.val == sum and root.left is None and root.right is None:
            return True
        else:
            left = self.hasPathSum(root.left,sum-root.val)
            right = self.hasPathSum(root.right,sum-root.val)
            return left or right
        