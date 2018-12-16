
import numpy as np
from scipy.special import comb
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        # my answer two  迭代  计算C(m,n)
        # a = np.array([x for x in range(rowIndex+1)])
        # b = np.array([rowIndex]*10)
        # c = comb(b,a)
        # return c
        #   answer one  递归 超时……
    #     if rowIndex < 2:
    #         now = [1]*(rowIndex+1)
    #         return now
    #     else:
    #         now = [1]*(rowIndex+1)
    #         for i in range(1,len(self.getRow(rowIndex-1))):
    #             now[i] = self.getRow(rowIndex-1)[i] + self.getRow(rowIndex-1)[i-1]
    #         return now
        now = []
        for j in range(rowIndex + 1):
            now = [1]*(j + 1)
            if j > 1:
                for i in range(1, len(pre)):
                    now[i] = pre[i] +pre[i-1]
            pre = now
            now = []
        return pre

s = Solution()
n = 9
print(s.getRow(n))
