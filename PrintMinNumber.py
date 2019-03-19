# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) <= 1:
            return numbers
        temp = []
        res = 0
        for i in numbers:
            while i > 9:
                i = i//10
            temp.append(i)
        while len(temp):
            # num_min = min(temp)
            res = res * 10**len(numbers[temp.index(min(temp))]) + numbers[temp.index(min(temp))]
            temp.pop(temp.index(min(temp)))
        return temp
s = Solution()
num = []