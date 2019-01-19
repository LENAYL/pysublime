class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        digit = 1
        while n > digit*9*10**(digit-1):
            n -= digit*9*10**(digit-1)
            digit += 1
        a = (n-1) // digit
        b = (n-1) % digit
        num = 10 ** (digit-1) + a
        res = list(str(num))[b: b+1]
        return int(''.join(res))
s = Solution()
n = 11
print(s.findNthDigit(n))

