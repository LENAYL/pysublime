class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 0 or len(nums) == len(set(nums)):
            return False
        table = {}
        for i in range(len(nums)):
            if nums[i] in table:
                for j in table[nums[i]]:
                    if (i - j) <= k:
                        return True
                table[nums[i]].append(i)
            else:
                table[nums[i]] = [i]
        return False
s = Solution()
nums =  [1,2,3,1,3,3]
a = 2
print(s.containsNearbyDuplicate(nums, a))

