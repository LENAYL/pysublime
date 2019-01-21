class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return False
        table = {}
        res = 0
        flag = 0
        for i in set(s):
            table[i] = s.count(i)
            if table[i] > 1:
                res += table[i] // 2
            if table[i] % 2 == 1:
                flag += 1
        return res * 2 + 1 if flag != 0 else res * 2
a = Solution()
s = "abccccdd"
print(a.longestPalindrome(s))
