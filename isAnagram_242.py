class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) :
            return False
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in t:
            if i in dict:
                dict[i] -= 1
                if dict[i] < 0:
                    return False
            else:
                return False
        return sum(list(dict.values())) == 0
s = "aacc"
t = "ccac"
ss = Solution()
print(ss.isAnagram(s,t))

