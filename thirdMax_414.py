class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #   method 1
        # table = {}
        # for i in nums:
        #     if i in table:
        #         table[i] += 1
        #     else:
        #         table[i] = 1
        # new_nums = list(sorted(table))
        # return new_nums[-3] if len(new_nums) >= 3 else new_nums[-1]

#          method 2
        res = [-2**31-1, -2**31-1, -2**31-1]
        for i in nums:
            if i > res[0]:
                res[0], res[1], res[2] = i, res[0], res[1]
            elif i > res[1]:
                res[1], res[2] = i, res[1]
            elif i > res[2]:
                res[2] = i
        print(res)
        return res[-1] if res[2] != -2**31-1 else res[0]





s = Solution()
nums =[2,1,3,2,1]
print(s.thirdMax(nums))
