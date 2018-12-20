class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n:
            rem = n%25
            n = n // 25
            sum += 6*n + rem//5
        return sum

s = Solution()
n = 135
print(s.trailingZeroes(n))




        # quotient = n//10
        # rem = n%10
        # if rem >= 5:
        #     return (n//25 + quotient*2 + 1)
        # else:
        #     return (n//25 + quotient*2)


