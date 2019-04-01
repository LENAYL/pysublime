# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s) == 0:
            return s

        s = [i for i in s.split(' ')]
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ' '.join(s)
a = Solution()
array = 'I am a student.'
print(a.ReverseSentence(array))