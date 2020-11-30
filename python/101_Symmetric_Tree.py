# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        else:
            return self.isSameTree(root.left, root.right)

    def pre_visit(self, root):
        if not root:
            return "-"
        result = self.pre_visit(root.left)
        result = result + str(root.val)
        result = result + self.pre_visit(root.right)
        return result

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == q and p == None:
            return True
        elif p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
            else:
                return False
        else:
            return False