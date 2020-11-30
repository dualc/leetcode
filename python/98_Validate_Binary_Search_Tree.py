# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)

    def helper(self, node, lower=float("-inf"), upper=float("inf")):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not self.helper(node.left, lower, val):
            return False
        if not self.helper(node.right, val, upper):
            return False
        return True