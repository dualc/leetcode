# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret=[]
        p=root
        while p or stack:
            if p:
                stack.append(p)
                p=p.left
            else:
                p=stack.pop()
                ret.append(p.val)
                p=p.right
        return ret

class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        left=self.inorderTraversal(root.left)
        right=self.inorderTraversal(root.right)
        return left+[root.val]+right
        