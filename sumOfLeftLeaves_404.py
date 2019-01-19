# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []

        def sumleaf(root):
            if root is None:
                return res
            if root.left:
                if root.left.left is None and root.left.right is None:
                    res.append(root.left.val)
                sumleaf(root.left)
            if root.right:
                sumleaf(root.right)


        sumleaf(root)
        return sum(res)
        # res = []
        # def sumleaf(root):
        #     if root.left:
        #         res.append(root.left.val)
        #         sumleaf(root.left)
        #     if root.right:
        #         sumleaf(root.right)
        #     if root is None:
        #         return res
        # sumleaf(root)
        # return sum(res)

s =Solution()
root = TreeNode(1)
one_1 = TreeNode(2)
one_2 = TreeNode(3)
two_1 = TreeNode(4)
two_2 = TreeNode(5)
# two_3 = TreeNode(4)
# two_4 = TreeNode(3)
# three_1 = TreeNode(5)
# three_2 = TreeNode(6)
# three_3 = TreeNode(7)
# three_4 = TreeNode(8)
# three_5 = TreeNode(8)
# three_6 = TreeNode(7)
# three_7 = TreeNode(6)
# three_8 = TreeNode(5)
root.left = one_1
root.right = one_2
one_1.left = two_1
one_1.right = two_2
# one_2.left = two_3
# one_2.right = two_4
#
# two_1.left = three_1
# two_1.right = three_2
# two_2.left = three_3
# two_2.right = three_4
# two_3.left = three_5
# two_3.right = three_6
# two_4.left = three_7
# two_4.right = three_8
# root = TreeNode(1)
# one_1 = TreeNode(2)
# one_2 = TreeNode(2)
# two_1 = TreeNode(3)
# two_2 = TreeNode(4)
# two_3 = TreeNode(4)
# two_4 = TreeNode(3)
# three_1 = TreeNode(5)
# three_2 = TreeNode(6)
# three_3 = TreeNode(7)
# three_4 = TreeNode(8)
# three_5 = TreeNode(8)
# three_6 = TreeNode(7)
# three_7 = TreeNode(6)
# three_8 = TreeNode(5)
# root.left = one_1
# root.right = one_2
# one_1.left = two_1
# one_1.right = two_2
# one_2.left = two_3
# one_2.right = two_4
#
# two_1.left = three_1
# two_1.right = three_2
# two_2.left = three_3
# two_2.right = three_4
# two_3.left = three_5
# two_3.right = three_6
# two_4.left = three_7
# two_4.right = three_8
print(s.sumOfLeftLeaves(root))

