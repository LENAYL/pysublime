# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        res = self.helper(numbers)
        print(res)
        return res[len(num) // 2] if res.count(res[len(num) // 2]) > len(num) // 2 else 0

    def helper(self, num, left=None, right=None):
        if len(num) == 0:
            return None
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
num = [5,8,9,2,14,2,5,3,8,2,2,2,2,2,2,2,2,2]
print(s.MoreThanHalfNum_Solution(num))