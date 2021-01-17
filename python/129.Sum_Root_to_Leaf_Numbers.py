class Solution1(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def pathSums(root, cur_sum):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 10*cur_sum+root.val
            else:
                left = pathSums(root.left, 10*cur_sum+root.val)
                right = pathSums(root.right, 10*cur_sum+root.val)
                return left+right
        return pathSums(root, 0)

class Solution2(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = self.allPath(root)
        return reduce(lambda x, y: x + int(y), paths, 0)

    def allPath(self, root):
        if not root:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        left = self.allPath(root.left)
        right = self.allPath(root.right)
        leftPath = [str(root.val) + i for i in left]
        rightPath = [str(root.val) + j for j in right]
        return leftPath + rightPath