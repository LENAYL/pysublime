# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         # write code here
#         if len(numbers) <= 1:
#             return 0
#         dict = {}
#         for i in numbers:
#             if i in dict:
#                 dict[i] += 1
#             else:
#                 dict[i] = 1
#         # res = 0
#         for i in dict:
#             if dict[i] > len(numbers)//2:
#                 return i
#         return 0
# -*- coding:utf-8 -*-
class Solution:
    # def MoreThanHalfNum_Solution(self, numbers):
    #     # write code here
    #     return self.helper(numbers)[len(numbers) // 2]

    def helper(self, num, left=None, right=None):
        # if len(num) == 0:
        #     return None
        left = 0 if not isinstance(left, (int, float)) else left
        right = len(num) - 1 if not isinstance(right, (int, float)) else right
        if left < right:
            key = self.pivotkey(num, left, right)
            self.helper(num, left, key - 1)
            self.helper(num, key + 1, right)
        return num

    def pivotkey(self, num, left, right):
        key = num[left]
        while left < right:
            while left < right and num[right] >= key:
                right -= 1
            num[left], num[right] = num[right], num[left]
            while left < right and num[left] <= key:
                left += 1
            num[left], num[right] = num[right], num[left]
        return left


s = Solution()
num = [3,2,3,2,2,2,5,4,2]
# print(s.MoreThanHalfNum_Solution(num))
print(s.helper(num))