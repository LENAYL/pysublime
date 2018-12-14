class TreeNode:


    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isisSymmetric(self, p, q):
    #     if not q and not p:
    #         return True
    #     if q and not p:
    #         return False
    #     if p and not q:
    #         return False
    #     if p.val == q.val:
    #         l = self.isisSymmetric(q.left, p.left)
    #         r = self.isisSymmetric(q.right, p.right)
    #         return l and r
    #     else:
    #         return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False

        def isisSymmetric(p, q):
            if not q and not p:
                return True
            if p.val == q.val and q and p:
                l = isisSymmetric(q.left, p.right)
                r = isisSymmetric(q.right, p.left)
                return l and r
            else:
                return False
        # tem = root
        if root.left.val == root.right.val:
            return isisSymmetric(root.left, root.right)
        else:
            return False


s =Solution()
root = TreeNode(1)
one_1 = TreeNode(2)
one_2 = TreeNode(2)
two_1 = TreeNode(3)
two_2 = TreeNode(4)
two_3 = TreeNode(4)
two_4 = TreeNode(3)
three_1 = TreeNode(5)
three_2 = TreeNode(6)
three_3 = TreeNode(7)
three_4 = TreeNode(8)
three_5 = TreeNode(8)
three_6 = TreeNode(7)
three_7 = TreeNode(6)
three_8 = TreeNode(5)
root.left = one_1
root.right = one_2
one_1.left = two_1
one_1.right = two_2
one_2.left = two_3
one_2.right = two_4

two_1.left = three_1
two_1.right = three_2
two_2.left = three_3
two_2.right = three_4
two_3.left = three_5
two_3.right = three_6
two_4.left = three_7
two_4.right = three_8
print(s.isSymmetric(root))