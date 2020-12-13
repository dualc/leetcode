class Solution1(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==1:
            return TreeNode(inorder[0])
        if not inorder:
            return None
        find = False
        for i in range(len(preorder)):
            for j in range(len(inorder)):
                if preorder[i] == inorder[j]:
                    find = True
                    break
            if find:
                break
        
        val = preorder[i]
        left = self.buildTree(preorder[i:],inorder[0:j])
        right = self.buildTree(preorder[i:],inorder[j+1:])
        return TreeNode(val,left,right)

class Solution2(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root