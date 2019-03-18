# -*- coding:utf-8 -*-
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
    #     if k > len(tinput):
    #         return []
    #     print(self.helper(tinput))
    #     return self.helper(tinput)[:k]
    # def helper(self, num, left = None, right = None):
    #     left = 0 if not isinstance(left, (int, float)) else left
    #     right = len(num) - 1 if not isinstance(right, (int, float)) else right
    #     if left < right:
    #         key = self.pivotkey(num, left, right)
    #         self.helper(num, left, key-1)
    #         self.helper(num, key + 1, right)
    #     return num
    # def pivotkey(self, num, left, right):
    #     key_value = num[left]
    #     while left < right:
    #         while left < right and num[right] >= key_value:
    #             right -= 1
    #         num[right], num[left] = num[left], num[right]
    #         while left < right and num[left] <= key_value:
    #             left += 1
    #         num[right],num[left] = num[left], num[right]
    #     # num[left] = key_value
    #     return left
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k <= 0 or  k > len(tinput):
            return []
        print(self.helper(tinput))
        return self.helper(tinput)[:k]
    def helper(self, num):
        if len(num) == 1:
            return num
        mid = len(num)//2
        left = self.helper(num[:mid])
        right = self.helper(num[mid:])
        return self.merge(left, right)
    def merge(self, left, right):
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res = res + left[i:] + right[j:]
        return res
s = Solution()
num = [4,5,1,6,2,7,3,8]
k = 4
print(s.GetLeastNumbers_Solution(num, k))