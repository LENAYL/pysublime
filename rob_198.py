class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #method 1
        # last = 0
        # now = 0
        # for i in nums: last, now = now, max(last + i, now)
        # return now
        #  method 2

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        sum_n = [0] * (len(nums))
        sum_n[0] = nums[0]
        sum_n[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            sum_n[i] = max(sum_n[i - 1], sum_n[i - 2] + nums[i])
        return sum_n[-1]


s = Solution()
nums = [4,1,2,7,5,3,1]
print(s.rob(nums))
