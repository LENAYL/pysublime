class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #  method 1
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        return len(set(zip(pattern, str))) == len(set(pattern)) == len(set(str))
        # method 2
        # str = str.split(' ')
        # if len(pattern) != len(str):
        #     return False
        # dict = {}
        # # dict_1 = {}
        # for i in range(len(pattern)):
        #     if pattern[i] in dict:
        #         if dict[pattern[i]] != str[i]:
        #             return False
        #     else:
        #         dict[pattern[i]] = str[i]
        #         # dict_1[str[i]] = pattern[i]
        # list = []
        # for value in dict.values():
        #     list.append(value)
        # return len(list) == len(set(list))

s = Solution()
pattern = 'abba'
# str = "dog cat cat dog"
str = "dog dog dog dog"
print(s.wordPattern(pattern, str))
