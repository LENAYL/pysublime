class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # method 1
        # import math
        # return n > 0 and 3**round(math.log(n, 3)) == n

        # method 2
        return n > 0 and (3**19) % n == 0
        # while n > 1:
        #     res = n % 3
        #     n = n // 3
        #     if res != 0:
        #         return False
        #     else:
        #         self.isPowerOfThree(n)
        # return True
s = Solution()
n = 26
print(s.isPowerOfThree(n))
