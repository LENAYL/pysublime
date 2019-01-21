class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # new_nums = list(set(sorted(nums)))
        table = {}
        for i in nums:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        new_nums = list(sorted(table))
        return new_nums[-3]

        # if len(new_nums) < 3:
        #     return new_nums[-1] if nums.count(new_nums[0]) > 1 else new_nums[0]
        #
        # return new_nums[-3]



s = Solution()
nums = [1,1,2,2,2,3,3,3,4,4,4,5,6]
print(s.thirdMax(nums))
