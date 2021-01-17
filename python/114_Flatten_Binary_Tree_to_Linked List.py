# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            tmp = root.left
            while tmp.right!=None:
                tmp = tmp.right
            tmp.right = root.right
            root.right=root.left
            root.left=None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def _flatten(root):
            if not root:
                return None
            if root.left is None and root.right is None:
                return root
            left = _flatten(root.left)
            right = _flatten(root.right)
            if left:
                left.right = root.right
                root.right = root.left
                root.left = None
            return right or left

        _flatten(root)

