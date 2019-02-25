class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s)[1:-1].find(s)!= -1
        # def gongyue(x, y):
        #     min_res = min(x, y)
        #     for j in range(1, min_res+1):
        #         if (x%j == 0) and (y%j == 0):
        #             res = j
        #     return res
        #
        # if len(set(s)) == 1:
        #     return True
        # dict_s = {}
        # list_s = []
        # print(s+s)
        # print((s+s)[1:-1].find(s) )
        # for i in s:
        #     if i in dict_s:
        #         dict_s[i] += 1
        #     else:
        #         dict_s[i] = 1
        # for v in dict_s.values():
        #     list_s .append(v)
        # res = 0
        # temp = 0
        # for i in range(len(list_s)-1):
        #     res = gongyue(list_s[i] ,  list_s[i +1])
        #     if temp != 0 and temp == res :
        #         temp = res
        #     elif temp != 0:
        #         return False
        # return res != 1
a = Solution()
s = "abcabc"
print(a.repeatedSubstringPattern(s))

