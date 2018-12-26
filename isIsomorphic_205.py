#  method 2
# class Solution(object):
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         return self.isomorphic(s)==self.isomorphic(t)
#     def  isomorphic(self, t):
#         s=[]
#         d={}
#         for i in range(len(t)):
#             if t[i] not in d:
#                 d[t[i]]=i
#             s.append(d[t[i]])
#         return s


#  method 1
# class Solution(object):
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s) != len(t):
#             return False
#         if len(set(s)) != len(set(t)):
#             return False
#
#         table = dict()
#         for i, x in enumerate(s):
#             if x in table:
#                 if table[x] != t[i]:
#                     return False
#             else:
#                 table[x] = t[i]
#
#         return True
class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def issamestr(ss):
            if len(ss) < 2:
                return True
            else:
                list = [1] * len(ss)
                i = 0
                for j in range(1, len(ss)):
                    if ss[j - 1] == ss[j]:
                        list[i] += 1
                    else:
                        i += 1
            return list

        if len(s) == len(t):
            return issamestr(s) == issamestr(t)
        else:
            return False
a = Solution()
s = 'happy'
t = 'ahnnc'
print(a.isIsomorphic(s,t))