class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #  method  1  先统一大小写  再利用filter输出
        s = s.lower()
        l = list((filter(str.isalnum, s)))
        return l == l[::-1]

        # method  答案
        # s =''.join(filter(str.isalnum, s)).lower()
        # return s == s[::-1]
        # #  method  2

        # s1 = (filter(str.isalnum, s))
        # l = list(s1)
        # while len(l) > 1:
        #     endd = l.pop()
        #     start = l.pop(0)
        #     if start !=  endd and start != endd.upper() and start != endd.lower():
        #         return False
        # return True
        # s = s.lower()
        # l=[ ]
        # for i in s:
        #     if  'a'<= s <='z' or 0<= i < 10:
        #         l.append(i)
        # while len(l) > 1:
        #     endd = l.pop()
        #     start = l.pop(0)
        #     if start !=  endd and start != endd.upper() and start != endd.lower():
        #         return False
        # return True
a = Solution()
# s ="A man, a plan, a canal: Panama"
s2 = "A , c,a"
print(a.isPalindrome(s2))

