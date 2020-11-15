# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        return self.genTree(1,n)
    
    def genTree(self,start,end):
        if start>end:
            return [None]
        if start==end:
            return [TreeNode(start)]
        trees=[]
        for index in range(start,end+1):
            left_trees=self.genTree(start,index-1)
            right_trees=self.genTree(index+1,end)
            for i in left_trees:
                for j in right_trees:
                    tree=TreeNode(index,i,j)
                    trees.append(tree)
        return trees