class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):  #  每个节点的最大深度
            if  not root:
                return 0
            l = depth(root.left) + 1
            r = depth(root.right) + 1
            return max(l,r)
        if not root:
            return True
        ll = depth(root.left)
        rr = depth(root.right)
        if abs(ll -rr) > 1:   #  同一个节点的深度差超过1  不平衡
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)     # 递归
        #
        # return



        # if not root:
        #     return True
        # if root.left and root.right:
        #     l = self.isBalanced(root.left)
        #     r = self.isBalanced(root.right)
        # elif root.left:
        #     if root.left.left or root.left.right:
        #         return False
        # elif root.right:
        #     if root.right.left or root.right.right:
        #         return False
        # else:
        #     return True
        # return l and r



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
print(s.isBalanced(root))