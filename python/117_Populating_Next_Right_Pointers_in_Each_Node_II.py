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
        cur = root
        while cur.left or cur.right or cur.next:
            tmp = cur
            while tmp:
                if tmp.right and tmp.left:
                    tmp.left.next = tmp.right
                    if tmp.next:
                        tmp.right.next = self.get_first(tmp.next)
                else:
                    if tmp.left and tmp.next:
                        tmp.left.next = self.get_first(tmp.next)
                    elif tmp.right and tmp.next:
                        tmp.right.next = self.get_first(tmp.next)
                    else:
                        pass
                tmp = tmp.next
            cur = cur.left or cur.right or cur.next
        return root

    def get_first(self, tree):
        if not tree:
            return None
        level = tree.left or tree.right or self.get_first(tree.next)
        return level


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution2:
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