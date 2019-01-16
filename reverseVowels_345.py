class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        o_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        s = list(s)
        while left <= right:
            while left <= len(s)-1 and s[left] not in o_list:
                left += 1
            while right >= 0 and s[right] not in o_list:
                right -= 1
            if left <= right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
        # d = {'a', 'e', 'i', 'o', 'u'}
        # l, r = 0, len(s) - 1
        # # print(''.join(s))
        # s = list(s)
        # while l <= r:
        #     if s[l].lower() not in d:
        #         l = l + 1
        #     elif s[r].lower() not in d:
        #         r = r - 1
        #     else:
        #         s[l], s[r] = s[r], s[l]
        #         l = l + 1
        #         r = r - 1
        # return ''.join(s)

a = Solution()
b = ".,"
print(a.reverseVowels(b))
        # l = len(s)
        # left = 0
        # right = l - 1
        # n_list = [0] * l
        # o_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # while left <= right:
        #     if s[left] in o_list and s[right] in o_list:
        #         n_list[left] = s[right]
        #         n_list[right] = s[left]
        #     else:
        #         n_list[left] = s[left]
        #         n_list[right] = s[right]
        #     left += 1
        #     right -= 1
        # return ''.join(n_list)



