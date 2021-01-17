# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nums = []
        self.current = root
        self.last = None

    def next(self) -> int:
        while self.current or self.nums:
            if self.current:
                self.nums.append(self.current)
                self.current = self.current.left
            else:
                top = self.nums.pop()
                self.current = top.right
                if not self.nums:
                    self.last = top
                return top.val
        return self.last

    def hasNext(self) -> bool:
        return self.current or self.nums

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()