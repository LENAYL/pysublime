class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #method 2
        if len(nums) == 0 or len(nums) == len(set(nums)):
            return False
        table = {}
        for i in range(len(nums)):
            if nums[i] in table and (i - table[nums[i]]) <= k:
                return True
            table[i] = i
        return False


        #   method 1  将元素值为键 索引值为value，做list 存在dict  在字典中 判断是否存在<= k的时候
        # if len(nums) == 0 or len(nums) == len(set(nums)):
        #     return False
        # table = {}
        # for i in range(len(nums)):
        #     if nums[i] in table:
        #         for j in table[nums[i]]:
        #             if (i - j) <= k:
        #                 return True
        #         table[nums[i]].append(i)
        #     else:
        #         table[nums[i]] = [i]
        # return False
s = Solution()
nums =  [1,2,3,1,3,3]
a = 2
print(s.containsNearbyDuplicate(nums, a))

