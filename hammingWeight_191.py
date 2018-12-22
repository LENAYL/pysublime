class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        list = []
        while n:
            list.append(n%2)
            n = n//2
        return sum(list)
s = Solution()
n = 3
print(s.hammingWeight(n))
