class Solution:
    def arrangeCoins(self, n: 'int') -> 'int':
        if n <= 2:
            return 1
        left, right = 1, n
        while left <= right:
            mid = (left + right)//2
            if (mid*(mid+1)//2) < n < ((mid+1)*(mid+2)//2):
                return mid
            elif n < (mid*(mid+1)//2):
                right = mid
            else:
                left = mid

s = Solution()
n = 5
print(s.arrangeCoins(n))

