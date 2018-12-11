# class Solution:
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         ss = ''
#         while s[-1] != '':
#             ss = s.split(' ')
#             # return s.split(' ')
#             return ss
#         return 0
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = ''
        l = len(s)
        # while s[-1] != '':
        if len(s) != 0:
            ss = s.split(' ')
            # return len(s[-' 1])
            # return len(ss[-1])
            for i in reversed(ss):
                if i != '':
                    return len(i)
                    break
            return 0
        # else:
        #     return len(s)

        # return 0
a = Solution()
# b = 'hello world '
b = ''
print(a.lengthOfLastWord(b))
# s = 'ab,cde,fgh,ijk'
# print(s.split(','))
c = ''
print(c.split(' '))
print(len(c))