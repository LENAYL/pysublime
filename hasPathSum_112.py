class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # def sum_count(root, sum):
        #     if not root:
        #         return 0
        #     else:
        #         sum_l = root.val + sum_count(root.left, sum)
        #         sum_r = root.val + sum_count(root.right, sum)
        #     if sum_l == sum or sum_r == sum:
        #         return True
        # if not root:
        #     return False
        # else:
        #     l = sum_count(root.left ,sum)
        #     r = sum_count(root.right, sum)
        # return l or r
        if root is None:
            return False
        sum -= root.val
        if sum == 0:
            if root.left is None and root.right is None:
                return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)



        # return False or True
s = Solution()
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
# three_8 = TreeNode(5)
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
# two_4.right = three_8
sum = 6
print(s.hasPathSum(root, sum))
