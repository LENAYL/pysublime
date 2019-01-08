class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # method 1
        if num == 0:
            return 0
        if num <= 9:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
        # method 2
        # list = []
        # while num:
        #     r = num % 10
        #     num = num // 10
        #     list.append(r)
        # sum_list = sum(list)
        # if sum_list >= 10:
        #     l = self.addDigits(sum_list)
        #     return l
        # else:
        #     return sum_list

s = Solution()
num = 38
print(s.addDigits(num))