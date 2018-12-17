class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     while len(nums) > 1:
        #     # for i in range(len(nums)):
        #     # index = nums[(i+1):].index(nums[i])
        #         if nums[i] not in nums[(i+1):]:
        #             return nums[i]
        #         else:
        #             nums = [x for x in nums if x!=nums[i]]
        #             # nums.remove(nums[i])
        #             # nums.remove(nums[i])
        # return nums[0]
        #  超时
        # l = []
        # for i in nums:
        #     if i in l:
        #         l.pop(l.index(i))
        #     else:
        #         l.append(i)
        # return l[0]

        #  异或  得出不一样
        # a = 0
        # for i in nums:
        #     a = a ^ i
        # return a
        return sum(set(nums))*2 - sum(nums)
s = Solution()
l = [2,2,1]
# l = [1,9,2, 2,1,3,4,3,4]
print(s.singleNumber(l))