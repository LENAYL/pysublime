class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2:
            return True
        while n > 2:
            tem = n%2
            n = n//2
            if tem == 1:
                return False
        return True
s = Solution()
n = 20
print(s.isPowerOfTwo(n))