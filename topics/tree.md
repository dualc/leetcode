# Tree专题

目前Tree专题只做了前200以内的。


## 94. Binary Tree Inorder Traversal

### 题目
树的中序遍历

### 思路

树的中序遍历常见的解法有递归、栈， Morris 遍历三种解法。

### Accept
Accepted

## 95. Unique Binary Search Trees II
### 题目
给一个数 n，用 1~n 的数字，生成所有的二叉搜索树。

### 思路
### 递归求解
思路和求数组的全排列有点像，以一个数做根，剩余的数作为子树，再求子树。

需要注意的是因为是二叉搜索树，需要满足树的每个根节点大于左边的值，小于右边的值。

要得到所有的树其实就是，以1~n的每个数字作为根节点来求对应的树。很明显这里就需要一个循环从
1~n。

当取一个数i来作为根的时候，因为是有序的，左子树就是 1~i-1的数字生成的，右子数是 i+1~n，满足二叉搜索树定义。左右子树如何生成呢，重复这个过程，递归求解。

当左右都得到结果的时候，用左右的树和i组合一个树，就是一个满足条件的树了。左右返回的都是数组，显然就是两个循环。

### Accept
Accepted

## 96. Unique Binary Search Trees
### 题目
给出一个数n，得到所有用1~n的数字生成的二叉搜索树数目

### 思路


1.偷懒解法

求出所有的树，计算一下数目

2.动态规划

其实树的排列个数与数字本身无关，只与个数有关。比如1~3和3~6的树的个数是一样的，都是3个数的排列。

假设f(n)是n对应树的个数,r(x)是以x为根时，根的个数，比如r(1)就是以1为根，显然r(x)=1:
- f(0)=1
- f(1)=1
- f(2)=r(0)`*`f(2)+f(1-0)`*`r(1)`*`f(2-1)

得出通解
f(n)=$\sum_{i=0}^n$ r(i)*f(i-1)*f(n-i),i$\in$[0,n]

```
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        record={0:1,1:1,2:2}
        if n in record:
            return record[n]
        for x in range(3,n+1):
            t=0
            for i in range(1,x+1):
                a=record[i-1]
                b=record[x-i]
                t=t+a*b
            record[x]=t
        return record[n]
```
### Accept
Accepted

## 98.Validate Binary Search Tree
### 题目
验证树是否是二叉搜索树

### 思路
1.递归

定义一个最大值（无穷大）和最小值（无穷小），计算机可表示的最大值和最小值：float('inf')、float('-inf')。
判断根节点是否在这个范围内，如果在，则判断左子树是否在这个范围（-inf,root.val），右子树（root.val，inf）

2.中序遍历

访问的节点值应该大于上一个节点，而且这种比较具有传递性
比如[2,1,3]：
1 访问1，1前面没有值
2 访问2，2是大于1的
3 访问3，3是大于2的，3也大于1
中序遍历输出二叉搜索树时，因为搜索树的特性，输出的值是有序的，从小到大。利用这个特性可以用于最K小的值。

### Accept
NoAccepted
想着递归没递归出来

## 99. Recover Binary Search Tree
### 题目
二叉搜索树有2个节点调换了位置，还原二叉搜索树。o(1)空间占用
### 思路
Morris 遍历
### Accept
NoAccepted

## 100. Same Tree
### 题目 
判断两棵树是否相同
### 思路
根节点值相同，两棵树的左子树和右子树相同，递归判断
### Accept
Accepted

## 101. Symmetric Tree
### 题目 
判断两棵树是否对称
### 思路

1.递归

根节点值相同，两个树A，B，A的左子树和B的右子树相同，A的右子树和B的左子树相同，递归判断
和上一题思路一致，判断条件稍微调整一下
### Accept
Accepted

## 102. Binary Tree Level Order Traversal
### 题目 
二叉树层次遍历
### 思路
递归法比层次遍历复杂一些，需要考虑层次对不齐的问题。
以前层次遍历使用的这种写法，所以一开始没想到层次遍历的解法
```
class Solution:
    def levelVisit(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        level = [root]
        ret = []
        while level:
            node=level.pop(0)
            ret.append(node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        return ret
```

#### 递归
分别获取左右子树的层次遍历结果，然后合并返回
#### 层次遍历
队列每次保存的都是同一层次的节点，访问完毕后，访问下一层，代码比较直观
```
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        ret = []
        while level:
            up = []
            next_level = []
            for l in level:
                up.append(l.val)
                for tree in (l.left,l.right):
                    if tree:
                        next_level.append(tree)
            ret.append(up)
            level = next_level
        return ret
```

### Accept
Accepted

## 103. Binary Tree Zigzag Level Order Traversal

### 题目 
二叉树层次遍历

### 思路
和102一样，加个判断，从第0行开始，偶数行正序，基数行逆序，加个计数

### Accept
Accepted

## 104. Maximum Depth of Binary Tree
### 题目
求最大深度

### 思路

1.递归
```python
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1
```

### Accept
Accepted

## 105. Construct Binary Tree from Preorder and Inorder Traversal
### 题目
由前序和中序还原一棵二叉树
### 思路
取前序的第一个节点，在中序中，在这个节点的左边的就是左子树的节点，右边的就是右子树的节点。再求左右子树。
### Accept
Accepted

## 106. Construct Binary Tree from Inorder and Postorder Traversal
### 题目
由后序和中序还原一棵二叉树
### 思路
取后序的最后节点，在中序中，在这个节点的左边的就是左子树的节点，右边的就是右子树的节点。再求左右子树。

可以看到无论是前中，还是后中还原一棵树，必须要有中序遍历。前后序遍历无法确定一棵树，因为无法确定节点在左还是在右
### Accept
Accepted

## 107. Binary Tree Level Order Traversal II
### 题目
层次遍历树
### 思路
跟102，103思路类似，本题层次是自低向上的，在102的基础上倒序即可。
### Accept
Accepted

## 108. Convert Sorted Array to Binary Search Tree
### 题目
将有序数组转换成一棵二叉搜索树
### 思路
二分法，取数组的中间点，左边的为左子树的点，右边的为右子树点，然后再求左右子树
### Accept
Accepted

## 110. Balanced Binary Tree
### 题目
判断树是否是平衡二叉树
### 思路
算出左右子树的高度，高度差小于1，然后再判断左右子树是否平衡
### Accept
Accepted

## 110. Minimum Depth of Binary Tree
### 题目
计算树的最小高度
### 思路
算出左右子树的最小高度，取两者中的最小高度+1，即为最小高度。需要递归。
### Accept
Accepted

## 112. Path Sum
### 题目
求出一条路径，路径之和等于给定值
### 思路
sum每次减去节点的值，然后去左右子树判断是否满足sum
### Accept
Accepted

## 113. Path Sum II
### 题目
求出路径之和等于给定值的所有路径
### 思路
思路和112一样，sum每次减去节点的值，然后去左右子树判断是否满足sum。
计算出左右子树的路径，然后合并
### Accept
Accepted

## 114. Flatten Binary Tree to Linked List
### 题目
将二叉树扁平成链表
### 思路
遍历树，将每棵树转换成链表。递归解题思路非常符合直觉，先处理左右子树，
然后如果左子树存在，则将右子树连接到左子树的末尾，然后递归返回，处理上层树
```python
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
```
优化，不用每次寻找左子树的末尾节点，每次返回末尾节点
```python
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
```
### Accept
Accepted

## 116. Populating Next Right Pointers in Each Node
### 题目
将完美二叉树每个结点指向它右边的的节点
### 思路
没想出来，参考了下别的解法。
解法1是别人写的，每二层一处理，利用上层节点平移，感觉还挺巧妙的，
解法2是根据解法1的理解写的，没有别人简洁。
解法3是根据层次遍历写的。这个应该是通解，可以解117
### Accept
No

## 117. Populating Next Right Pointers in Each Node II
### 题目
将二叉树每个结点指向它右边的的节点，和116的区别是，树不一定是完美二叉树
### 思路
解法1 写的很纠结，那时候没想到这种层次遍历写法
解法2 层次遍历，完美通吃116和117
### Accept
Accept

## 124. Binary Tree Maximum Path Sum
### 题目
求二叉树的最大路径
### 思路
没有写出来，一开始题目也没有太理解。参考了下别人的解法，
递归，计算每棵树的最大路径：
 1. 首先计算左右子树路径
 2. 选择左右子树的最大路径加上根节点的路径，就是当前子树的最大路径，返回路径值
### Accept
No Accept

## 129. Sum Root to Leaf Numbers
### 题目
求出从根到叶子组成的数的和
### 思路
### 解法1
递归，从根递归到叶子，计算出每棵树的和:
 1. 计算左右子树的和
 2. 计算当前子树的和：左右子树的和相加

### 解法2
求出所有从根到叶子组合成的字符串
最后得到是一个字符串数组，转换成数字，求它们的和。相比解法1更直观一些

## 144. Binary Tree Preorder Traversal
### 题目
树的前序遍历

### Accept
Accept

## 145. Binary Tree Postorder Traversal
### 题目
树的后序遍历
### Accept
Accept

## 173. Binary Search Tree Iterator
### 题目
按照中序实现一个二叉树迭代器
### 思路
可以按照树实现的中序遍历算法实现。递归和使用栈两种方式。
### 递归
先中序遍历一遍，保存在数组中，然后用迭代器访问。
递归不受控，无论访问什么，首先得先递归保存节点。比如第一次next就得先遍历一遍。
### 栈
以栈的方式遍历树，遍历到那里是那里，相对递归法时间复杂度底。
### Accept
Accept

## 199. Binary Tree Right Side View
### 题目
从右边看一棵树，从上到下看到的节点
### 思路
#### 层次遍历
层次遍历，取每层得最后一个节点。跟116和117相似
#### 递归
求出每层的节点，最后每层取最后一个
### Accept
Accept