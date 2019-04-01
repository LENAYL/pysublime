# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        temp_list = []
        max_mult = 2**31
        res = []
        for i in range(len(array)):
            if (tsum - array[i]) in temp_list:
                temp = array[i] * (tsum - array[i])
                if max_mult > temp:
                    res = [(tsum - array[i]), array[i]]
            else:
                temp_list.append(array[i])

        return res
s = Solution()
num = [1,2,4,7,11,15]
n = 15
print(s.FindNumbersWithSum(num, n))