# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if root and root.val == sum and root.left is None and root.right is None:
            return [[root.val]]
        else:
            left = self.pathSum(root.left, sum - root.val)
            right = self.pathSum(root.right, sum - root.val)
            paths = left + right
            ret = []
            for path in paths:
                if path:
                    ret.append([root.val] + path)
            return ret