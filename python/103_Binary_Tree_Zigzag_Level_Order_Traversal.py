# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.levelOrder(root, 0)

    def levelOrder(self, root, height):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        val = [root.val]
        left = self.levelOrder(root.left, height + 1)
        right = self.levelOrder(root.right, height + 1)
        left = filter(lambda x: x != [], left)
        right = filter(lambda x: x != [], right)
        left_len = len(left)
        right_len = len(right)
        level = []
        for l in range(min(left_len, right_len)):
            if (height + l + 1) % 2 == 0:
                level.append(left[l] + right[l])
            else:
                level.append(right[l] + left[l])
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