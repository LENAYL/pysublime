# -*- coding:utf-8 -*-
# class Solution:
#     def Add(self, num1, num2):
#         # write code here
#         mask = 0xffffffff
#         MAX = 0x7fffffff
#         while num2:
#             num1 = (num1 ^ num2)
#             num2 = ((num1 & num2) << 1)
#             num1 = num1 & mask
#             num2 = num2 & mask
#         return num1 if num1 <= MAX else ~(num1 ^ mask)
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        MAX = 0x7fffffff
        mask = 0xffffffff
        while num2:
            num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
            num1 = num1 & mask
            num2 = num2 & mask
        return num1 if num1 <= MAX else ~(num1 ^ mask)
s = Solution()
n1 = -1
n2 = 1
print(s.Add(n1, n2))