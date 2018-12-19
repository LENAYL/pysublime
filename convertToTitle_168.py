class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dict = {1: 'A', 2:'B', 3:'C', 4:'D',5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10: 'J', 11: 'K', 12: 'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
        res = ''
        # method 1
        # while n:
        #     index = n%26   #余数
        #     n = n // 26  # 商
        #     if index != 0:
        #         res = res + ''.join(dict[index])
        #     else:
        #         res = res + ''.join(dict[index+26])
        #         n -= 1
        # return res
        # method 2
        while n:
            if n%26 == 0:
                res += dict[26]
                n -= 1
            else:
                res += dict[n%26]
            n = n//26
        return res
s = Solution()
n = 701
print(s.convertToTitle(n))




