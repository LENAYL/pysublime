# 暴力计算 over 78%
# class Solution:
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         # dic = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
#         # strs = ['1']
#         # strs[0] = '1'
#         # i = 0
#         # j = 1
#         # t = 0
#         # for k in range(1,31):
#         #     for i in range(0,len(strs[k-1])-1):
#         #         if strs[k-1][i] == strs[k-1][i+1]:
#         #             j += 1
#         #         else:
#         #             new_strs[t] = j
#         #             new_strs[t+1] = strs[k-1][i]
#         #             t += 2
#         #             j = 1
#         #             strs.append(new_strs)
#         # return strs[n-1]
#         # d = {'1': '1'}
#         # d = ['1', '123','11254']
#         d = ['1',]
#         if n == 1:
#             return 1
#         if n < 1:
#             return False
#         # k = 1
#         for k in range(1,31):
#             if k <= len(d):
#                 s = d[k-1] + '0'
#                 # print(s)
#                 # print(type(s))
#                 # print(s.join('0'))
#                 # s.append(0)
#                 j = 1
#                 # t = 0
#                 new = ''
#                 for i in range(0, len(s)-1):
#                     if s[i] == s[i+1]:
#                         j += 1
#                     else:
#                         new = new + str(j) +s[i]
#
#                         # new.insert(-1,j)
#                         # new.insert(-1,s[i])
#                         # t += 2
#                         j = 1
#                 d.append(new)
#         return d[n-1]
# ss = Solution()
# print(ss.countAndSay(5))



# 函数迭代   over 94%
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        # pre = '11'
        def myconutandsay(self, nums, t):
            j = 1
            new = ''
            for k in range(0,(len(nums)-1)):
                if nums[k] == nums[k+1]:
                    j += 1
                else:
                    new = new + str(j) + nums[k]
                    j = 1
            new = new + str(j) + nums[k+1]
            if t == n:
                return new
            else:
                return myconutandsay(self, new, (t+1))
        return myconutandsay(self, '11', 3)

ss = Solution()
print(ss.countAndSay(8))




