# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        print(self.helper(tinput))
        return self.helper(tinput)[:k]
    def helper(self, num, left = None, right = None):
        left = 0 if not isinstance(left, (int, float)) else left
        right = len(num) - 1 if not isinstance(right, (int, float)) else right
        if left < right:
            key = self.pivotkey(num, left, right)
            self.helper(num, left, key-1)
            self.helper(num, key + 1, right)
        return num
    def pivotkey(self, num, left, right):
        key_value = num[left]
        while left < right:
            while left < right and num[right] >= key_value:
                right -= 1
            num[right], num[left] = num[left], num[right]
            while left < right and num[left] <= key_value:
                left += 1
            num[right],num[left] = num[left], num[right]
        # num[left] = key_value
        return left
s = Solution()
num = [4,5,1,6,2,7,3,8]
k = 10
print(s.GetLeastNumbers_Solution(num, k))