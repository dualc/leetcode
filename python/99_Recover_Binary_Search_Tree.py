# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        x=y=None
        pre=None
        while root:
            if root.left:
                pretree=root.left
                while pretree.right!=None and pretree.right!=root:
                    pretree=pretree.right
                if pretree.right is None:
                    pretree.right=root
                    root=root.left
                else:
                    if pre and pre.val > root.val:
                        y = root
                        if x is None:
                            x=pre
                    pre=root
                    pretree.right=None
                    root = root.right
            else:
                if pre and pre.val>root.val:
                    y=root
                    if x is None:
                        x=pre
                pre=root
                root = root.right
        if x and y:
            x.val,y.val=y.val,x.val