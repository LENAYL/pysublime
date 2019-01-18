class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        table = []
        for i in ransomNote:
            if i not in table:
                if i in magazine and (ransomNote.count(i) <= magazine.count(i)):
                    pass
                else:
                    return False
                table.append(i)
        return True
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         if len(ransomNote) > len(magazine):
#             return False
#         r_table = {}
#         m_table = {}
#         for i in ransomNote:
#             if i not in r_table:
#                 r_table[i] = 1
#             else:
#                 r_table[i] += 1
#         for i in magazine:
#             if i not in m_table:
#                 m_table[i] = 1
#             else:
#                 m_table[i] += 1
#         for key in r_table:
#             if key not in magazine or (key in magazine and r_table[key] > m_table[key]) :
#                 return False
#             # elif key in magazine and r_table[key] > m_table[key]:
#             #     return False
#         return True
s = Solution()
r = "ac"
m = "ab"
print(s.canConstruct(r, m))
print(m.count('c'))





