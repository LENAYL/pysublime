class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left = 1
        right = num
        while left < (right-1):
            mid = (right + left) // 2
            if mid * mid > num:
                right = mid

            elif mid * mid  < num:
                left = mid
            else:
                return True
        return False

s = Solution()
num = 100
print(s.isPerfectSquare(num))