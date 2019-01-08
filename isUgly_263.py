class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = abs(num)
        list = [2, 3, 5]
        while num > 5:
            j = 0
            for i in range(len(list)):
                if num % list[i] == 0:
                    num = num // list[i]
                    break
                else:
                    j += 1
                if j == 3:
                    return False
        return True
s = Solution()
num = 75
print(s.isUgly(num))