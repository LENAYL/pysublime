# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) < 5:
            return False
        new_num = [i for i in numbers if i > 0]
        new_num.sort()
        n = 0
        for i in range(len(new_num)-1):
            if (new_num[i+1] - new_num[i]) > 0:
                n += (new_num[i+1] - new_num[i])
            else:
                return False
        if n < 5:
            return True
        else:
            return False