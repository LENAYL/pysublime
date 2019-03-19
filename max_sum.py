# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return None
        temp_sum = 0
        res = -2**31
        for i in array:
            if temp_sum < 0:
                temp_sum = i
            else:
                temp_sum += i
            res = max(res, temp_sum)
        return res
s = Solution()
num = [6, -3, -2, 7, -15, 1, 2, 2]
print(s.FindGreatestSumOfSubArray(num))