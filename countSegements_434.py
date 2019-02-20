class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        return len(s)
a = Solution()
string = 'hello, jorn how are you ?'
print(a.countSegments(string))
