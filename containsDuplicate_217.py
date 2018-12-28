class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        # if len(nums) == 0:
        #     return False
        # table = {}
        # for i in range(len(nums)):
        #     if nums[i] not in table:
        #         table[nums[i]] = i
        #     else:
        #         return True
        # return  False
s = Solution()
nums = [1, 2, 2, 3, 4]
print(s.containsDuplicate(nums))
