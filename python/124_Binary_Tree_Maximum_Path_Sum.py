# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def calTree(root):
            if not root:
                return 0
            left = max(calTree(root.left), 0)
            right = max(calTree(root.right), 0)
            maxSum = root.val + left + right
            self.maxSum = max(self.maxSum, maxSum)
            return max(left, right) + root.val

        calTree(root)
        return self.maxSum