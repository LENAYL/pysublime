class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #  method 1  快
        dict = {}
        for i in range(len(numbers)):
            if (target - numbers[i]) in dict:
                return (dict[target - numbers[i]], i+1)
            dict[numbers[i]] = i +1
        #  method  2  慢……
        # dict = {}
        # if len(numbers) > 1:
        #     for i in range(len(numbers)):
        #         dict[numbers[i]] = i+1
        #     for j in dict.keys():
        #         res = target - j
        #         if res in dict.keys():
        #             key1 = dict.get(j)
        #             key2 = dict.get(res)
        #             if key1 < key2:
        #                 return key1, key2
        #             elif key1 == key2:
        #                 return key1-1, key2
        #             else:
        #                 return key2, key1
s = Solution()
# nums =  [2, 7, 11, 15]
# sum = 9
nums = [0,0,3,4]
sum = 0
print(s.twoSum(nums, sum))
