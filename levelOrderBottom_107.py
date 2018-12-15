# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     global list
#     list = []
#     def levelOrderBottom(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         global list
#         if not root:
#             return None
#
#         if root.left and root.right:
#             list.append(self.levelOrderBottom(root.left))
#             list.append(self.levelOrderBottom(root.right))
#         elif root.left and not root.right:
#             list.append(self.levelOrderBottom(root.left))
#         elif root.right and not root.left:
#             list.append(self.levelOrderBottom(root.right))
#         else:
#             return root.val
        # print(list)
    # return list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # bfs广度优先搜索，不熟悉可以网上参考bfs代码
        if not root:
            return []  # 为空则返回空列表
        queue = [root]  # 使用列表实现队列的功能，首先存储root
        res = []
        while queue:  # 当queue不为空时
            nodes = []  # 存节点，每次循环前置空，每次只装一部分
            node_values = []  # 存节点的值
            for node in queue:
                if node.left:
                    nodes.append(node.left)  # 将左子树装入队列中
                if node.right:
                    nodes.append(node.right)
                node_values += [node.val]  # 因为每次循环node_values都会置空，所以最终结果保存在res里，node_values只是一小部分结果
            res = [node_values] + res  # 实现从底到顶，node_values放前面.
            queue = nodes  # 将新添加的节点重新赋值给queue
        return res


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
print(s.levelOrderBottom(root))
# print(list)

