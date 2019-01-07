# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # method 1
        if root is not None:
            if p.val < root.val and q.val >= root.val:
                return root.val
            elif p.val <= root.val and q.val <= root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)
        # if (p <= root.val and q >= root.val) or (q <= root.val and p >= root.val):
        #     return root.val
        # elif p <= root.val and q <= root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return self.lowestCommonAncestor(root.right, p, q)
#         method 2
#         if root is not None:
#             if root.val > max(p.val, q.val):
#                 return self.lowestCommonAncestor(root.left, p, q)
#             elif root.val < min(p.val, q.val):
#                 return self.lowestCommonAncestor(root.right, p, q)
#             else:
#                 return root.val
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

p = TreeNode(2)
q = TreeNode(6)
print(s.lowestCommonAncestor(root, p, q))
