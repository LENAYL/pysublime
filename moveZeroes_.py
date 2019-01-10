# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         # old_l = len(nums)
#         # nums = set(nums)
#         nums.sort()
#         if nums[-1] == 0:
#             nums[:] = nums
#         # l = len(nums)
#         i = 0
#         if i in nums:
#             first = nums.index(0)
#             left = first
#             right = len(nums)-1
#
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] > 0:
#                     right = mid -1
#                 elif nums[mid] == 0 and nums[mid+1] > 0:
#
#                     left = len(nums)
#                 else:
#                     left = mid + 1
#             nums[:] = nums[: first] + nums[mid+1:] + nums[first: mid + 1]
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # method 2
        i = 0
        l = len(nums)
        lens = len(nums)
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
            else:
                i += 1
        lens = lens - len(nums)
        for j in range(lens):
            nums.append(0)
        # method 1
        i = 0
        while i in nums:
            first = nums.index(0)
            nums.append(nums.pop(first))
        # nums.sort()
        # # l = len(nums)
        # if nums[-1] == 0 :
        #     nums[:] = nums
        # else:
        #     i = 0
        #     if i in nums:
        #         first = nums.index(0)
        #         left = first
        #         right = len(nums)-1
        #
        #         while left <= right:
        #             mid = (left + right) // 2
        #             if nums[mid] > 0:
        #                 right = mid -1
        #             elif nums[mid] == 0 and nums[mid+1] > 0:
        #
        #                 left = len(nums)
        #             else:
        #                 left = mid + 1
        #         nums[:] = nums[: first] + nums[mid+1:] + nums[first:  mid+ 1]
        #     else:
        #         nums[:] = nums
s = Solution()
# nums = [1, 2, 4, -7, 0, 0, 8, 7, 0, -8]
nums = [2,1]
print(s.moveZeroes(nums))

