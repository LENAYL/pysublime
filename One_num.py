# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        mult, res = 1, 0
        num = 1
        while n//mult:
            high, mod = divmod(n, mult*10)
            cur, low = divmod(mod, mult)
            if cur > num:
                res += high * mult + mult
            elif cur == num:
                res += high * mult + low +1
            else:
                res += high * mult
            mult = mult * 10
        return res