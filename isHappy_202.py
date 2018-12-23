class Solution(object):
    # import sys
    # sys.setrecursionlimit(1000000)
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
#  只要出现4 就被不是快乐数  list1 = [4,16, 37, 58, 89, 145,42, 20]  不快乐数
       #method 1  递归
        # if n == 1:
        #     return True
        # else:
        #     tem = n
        #     list = []
        #     while tem != 0:
        #         list.append(tem%10)
        #         tem = tem // 10
        #     sum = 0
        #     for i in list:
        #         sum = sum + pow(i, 2)
        #     if sum == 4:
        #         return False
        #     return self.isHappy(sum)

        #method 2
        cir = 10
        for i in range(cir):
            sum = 0
            while n != 0:
                sum += pow(n%10, 2)
                n = n//10
            if sum == 1:
                return  True
            else:
                n = sum
        return False


s =Solution()
n = 2
print(s.isHappy(n))


