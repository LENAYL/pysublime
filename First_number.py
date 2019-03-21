# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) < 1:
            return -1
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in dict:
            if dict[i] == 1:
                return s.index(i)
        return -1
a = Solution()
s = 'NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp'
print(a.FirstNotRepeatingChar(s))