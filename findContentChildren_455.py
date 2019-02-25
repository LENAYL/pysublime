class Solution:
    def findContentChildren(self, g: 'List[int]', s: 'List[int]') -> 'int':
        g.sort()
        s.sort()
        count =0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count
        # count = 0
        # g_len = len(g)
        # s_len = len(s)
        # len_min = min(len(g), len(s))
        # while len_min:
        #     if g.pop(g.index(min(g))) <= s.pop(s.index(min(s))):
        #         count += 1
        #         len_min -= 1
        #     else:
        #         return count
a = Solution()
g_g = [1,2,3]
s_s = [3,2,1,1,2,2,3]
print(a.findContentChildren(g_g,s_s))
