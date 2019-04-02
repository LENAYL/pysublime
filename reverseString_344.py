class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]

        j = len(s)-2
        new_s = s[-1]
        while j >= 0:
            new_s += s[j]
            j -= 1
            # temp = s[j]
            # s[j] = s[i]
            # s[i] = temp
        return new_s
a = Solution()
b = "hello"
print(a.reverseString(b))