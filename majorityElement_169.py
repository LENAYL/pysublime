class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]
        # 慢慢慢
        # dict = {}
        # list = []
        # for i in nums:
        #     if i in dict:
        #         dict[i] += 1
        #         if dict[i] > (len(nums)//2):
        #             list.append(i)
        #     else:
        #         dict[i] = 1
        # return list
s = Solution()
nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))