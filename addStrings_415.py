class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # dict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
        # num1 = num1.split()
        # num2 = num2.split()
        # for i in num1:
        #     print(i)
        i = 0
        j = 0
        jinwei = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ''
        while i < len(num1) and j < len(num2):
            temp = int(num1[i]) + int(num2[j]) + jinwei
            res += str(temp % 10)
            jinwei  = temp // 10
            i += 1
            j += 1
        while i < len(num1):
            temp = int(num1[i]) + jinwei
            res += str(temp % 10)
            jinwei = temp // 10
            i += 1
        while j < len(num2):
            temp = int(num2[j]) + jinwei
            res += str(temp % 10)
            jinwei = temp // 10
            j += 1
        if jinwei:
            res += str(jinwei)
        return res[::-1]


s = Solution()
a = '1014'
b = '14'
print(s.addStrings(a, b))

