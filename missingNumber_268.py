class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_num = sum(nums)
        return int(n*(n+1)/2 - sum_num)
s = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))