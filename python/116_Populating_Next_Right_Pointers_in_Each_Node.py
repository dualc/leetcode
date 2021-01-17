"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution1(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        cur=root
        while cur.left:
            tmp=cur
            while tmp:
                tmp.left.next=tmp.right
                if tmp.next:
                    tmp.right.next=tmp.next.left
                tmp=tmp.next
            cur=cur.left
        return root

class Solution2(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        pre = root
        last=None
        head=None
        while pre:
            for tree in [pre.left,pre.right]:
                if not tree:
                    continue
                if not head:
                    head = tree
                if last:
                    last.next=tree
                last=tree
            pre=pre.next
            if not pre:
                pre=head
                last=None
                head=None
        return root

class Solution3:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        level = [root]
        while level:
            pre=None
            next_level = []
            for node in level:
                if not node:
                    continue
                if node and pre:
                    pre.next=node
                pre = node
                next_level.append(node.left)
                next_level.append(node.right)
            level=next_level
        return root