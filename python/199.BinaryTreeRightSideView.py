# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        level=[root]
        view=[]
        while level:
            view+=[level[-1].val]
            next_level=[]
            for l in level:
                for tree in [l.left,l.right]:
                    if tree:
                        next_level.append(tree)
            level=next_level
        return view


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        level = self.getLevelTree(root)
        ret = []
        for i in level:
            ret.append(i[-1])
        return ret

    def getLevelTree(self, root):
        if not root:
            return []
        left = self.getLevelTree(root.left)
        right = self.getLevelTree(root.right)
        min_len = min(len(left), len(right))
        level = []
        for i in range(min_len):
            level.append(left[i] + right[i])
        if min_len < len(left):
            level.extend(left[min_len:])
        if min_len < len(right):
            level.extend(right[min_len:])
        return [[root.val]] + level