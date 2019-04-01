# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) == 0:
            return None
        dict = {}
        for i in range(len(array)):
            if array[i] in dict:
                dict[array[i]] += 1
                if dict[array[i]] == 2:
                    del dict[array[i]]
            else:
                dict[array[i]] = 1
        return [i for i in dict]
s = Solution()
num = [1,2,3,4,5,2,3,4]
print(s.FindNumsAppearOnce(num))
