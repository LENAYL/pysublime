class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if not nums:
            return None
        root = TreeNode(nums[length // 2])
        root.left = self.sortedArrayToBST(nums[:length // 2])
        root.right = self.sortedArrayToBST(nums[length // 2 + 1:])
        return root


# class Solution:
#     global list_left
#     global list_right
#     def sortedArrayToBST(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """
#         def find_root(list):
#             n = len(list)
#             global list_left
#             list_left = []
#             global list_right
#             list_right = []
#             # if n/2 == 1:
#             x = list[int(n/2)]
#             list_left = list[:int(n/2)]
#             list_right = list[int(n / 2):]
#             if len(list[:int(n/2)]) > 0 and len(list[int(n / 2):]) > 0:
#                 # if len(list_left) > 0 and len(list_right) > 0:
#                 x.left = find_root(list_left)
#                 x.right = find_root(list_right)
#             elif len(list[int(n / 2):]) > 0:
#                 x.right = find_root(list_right)
#             elif len(list[:int(n/2)]) > 0 :
#                 x.left = find_root(list_left)
#             else:
#                 return x
#
#             # return x
#         if len(nums) == 0:
#             return False
#         else:
#             return find_root(nums)
s = Solution()
nums = [-10,-3,0, 1,5,9]
print(s.sortedArrayToBST(nums))

