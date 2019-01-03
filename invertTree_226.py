# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.left or root.right:
            tem = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
            root.left = tem
        return root

root = TreeNode(4)
a = TreeNode(2)
b = TreeNode(7)
c = TreeNode(1)
d = TreeNode(3)
e = TreeNode(6)
f = TreeNode(9)

root.right = b
root.left = a
a.left = c
a.right = d
c.right = None
c.left = None
d.right = None
d.left = None

b.left = e
b.right = f
e.right = None
e.left = None
f.right = None
f.left = None

s = Solution()
print(s.invertTree(root))