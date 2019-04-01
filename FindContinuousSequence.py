# -*- coding:utf-8 -*-
import math
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
# method 1
        # temp = []
        # temp_sum = 0
        # res = []
        # for i in range(1, int(math.ceil(tsum/2))+1):
        #     temp.append(i)
        #     temp_sum += i
        #     if temp_sum == tsum:
        #         res.append(list(temp))
        #         temp_sum = 0
        #         temp = []
        #     elif temp_sum < tsum:
        #         continue
        #     else:
        #         while temp_sum > tsum:
        #             temp_sum -= temp.pop(0)
        #         if temp_sum == tsum:
        #             res.append(list(temp))
        #             temp_sum = 0
        #             temp = []
        # return res
        # method 2
        left = 1
        right = 2
        res = []
        for i in range(1, int(math.ceil(tsum))+1):
            temp_sum = (left + right) *(right - left +1) // 2
            if temp_sum < tsum:
                right += 1
            elif temp_sum > tsum:
                left += 1
            else:
                temp = []
                for i in range(left, right+1):
                    temp.append(i)
                res.append(list(temp))
                left += 1
        return res


s = Solution()
n = 100
print(s.FindContinuousSequence(n))
