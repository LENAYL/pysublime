# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:  # 为空，直接返回[]
            return []
        res = []

        # temp=''

        def recursive(root, temp=''):
            # global temp
            temp += str(root.val)
            if not root.left and not root.right:  # 左右子树皆为空时
                res.append(temp)
            temp += '->'
            if root.left:
                recursive(root.left, temp)
            if root.right:
                recursive(root.right, temp)

        recursive(root)  # 调用递归
        return res
s  = Solution()
root = TreeNode(6)
a = TreeNode(2)
b = TreeNode(8)
c = TreeNode(0)
d = TreeNode(4)
e = TreeNode(3)
f = TreeNode(5)
g = TreeNode(7)
h = TreeNode(9)

root.left = a
root.right = b
a.left = c
a.right = d
d.right = f
d.left = e
b.left = g
b.right = h
print(s.binaryTreePaths(root))