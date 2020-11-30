# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        val = [root.val]
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        left = filter(lambda x: x != [], left)
        right = filter(lambda x: x != [], right)
        left_len = len(left)
        right_len = len(right)
        level = []
        for l in range(min(left_len, right_len)):
            level.append(left[l] + right[l])
        left_rest = right_rest = []
        if left_len > right_len:
            left_rest = left[len(level):]
        if left_len < right_len:
            right_rest = right[len(level):]
        ret = [val] + level
        if left_rest:
            ret.extend(left_rest)
        if right_rest:
            ret.extend(right_rest)
        return ret
