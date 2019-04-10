# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size > len(num) or len(num) == 0 or size < 1:
            return None
        if size  == 1:
            return num
        temp = []
        res = []
        for i in range(len(num)):
            if len(temp) > 0 and  i - temp[0] > (size -1):
                temp.pop(0)
            while len(temp) > 0 and num[i] > num[temp[-1]]:
                temp.pop()
            if len(temp) < size - 1:
                temp.append(i)
            if i >= size -1:
                res.append(num[temp[0]])
        return res
s = Solution()
num = [16,14,12,10,8,6,4]
k = 0
print(s.maxInWindows(num, k))