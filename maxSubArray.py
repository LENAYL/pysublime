# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i = 0
#         index_nums = []
#         for j in nums:
#             if j < 0:
#                 index_nums[i] = nums.index(j)
#                 i += 1
# i = 0
# nums = [-2,1,-3,4,-1,2,1,-5,4]

# print(nums[1:])
# index_nums = []
# for j in nums:
#     if j < 0:
#         index_nums.append(nums.index(j))
#
#         # i += 1
# print(index_nums)
# new_list = []
# # for i in range(0,len(index_nums)-1):
# #     for j in range(i,len(index_nums))
# #     if (index_nums[i+1] - index_nums[i]) != 1:
# #         new_list.append(nums[(index_nums[i]+1):(index_nums[i+1])])
# # new_list.append(nums[(index_nums[-1]+1):])
# # print(new_list)
# for i in range(0,len(index_nums)-1):
#     for j in range(i+1,len(index_nums)):
#         print(i,j)
#         if (index_nums[i ] - index_nums[j]) != 1:
#             new_list.append(nums[(index_nums[i] + 1):(index_nums[j])])
#     # if
#     new_list.append(nums[(index_nums[i] + 1):])
# print(new_list)
# # max = 0
# max_list = []
# for k in range(0,len(new_list)):
#     max_list.append(sum(new_list[k]))
# # print(new_list[max_list.index([max(max_list)])])
# print(max_list)
# print(max(max_list))
# print(new_list[max_list.index(max(max_list))])
# nums = [1,2,-1,-2,2,1,-2,1]
# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # for i in
#         index_nums = []
#         posi_nums = []
#         # for i in nums:
#         for i in range(0,len(nums)):
#             if nums[i] < 0:
#                 index_nums.append(i)
#             else:
#                 posi_nums.append(i)
#         if len(posi_nums) == len(nums):
#             return sum(nums)
#         if len(index_nums) == len(nums):
#             return max(nums)
#         if len(posi_nums) == 1:
#             return nums[posi_nums[0]]
#         if len(index_nums) == 1:
#             return max(sum(nums[:index_nums[0]]), sum(nums[index_nums[0]:]))
#         new_list = []
#         for i in range(0,len(index_nums)-1):
#             for j in range(i+1,len(index_nums)):
#                 # print(i,j)
#                 if (index_nums[i ] - index_nums[j]) != 1:
#                     new_list.append(nums[(index_nums[i] + 1):(index_nums[j])])
#     # if
#             new_list.append(nums[(index_nums[i] + 1):])
#             new_list.append(nums[:index_nums[i]])
#         print(new_list)
#         max_list = []
#         for k in range(0,len(new_list)):
#             max_list.append(sum(new_list[k]))
#         print(max_list)
#         print(max(max_list))
#         print(new_list[max_list.index(max(max_list))])
#         return(max(max_list))
# nums = [-1,0,-2,2]
# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # for i in
#         index_nums = []
#         posi_nums = []
#         # for i in nums:
#         for i in range(0,len(nums)):
#             if nums[i] < 0:
#                 index_nums.append(i)
#             else:
#                 posi_nums.append(i)
#         if len(posi_nums) == len(nums):
#             return sum(nums)
#         if len(index_nums) == len(nums):
#             return max(nums)
#         if len(posi_nums) == 1:
#             return nums[posi_nums[0]]
#         if len(index_nums) == 1:
#             return max(sum(nums[:index_nums[0]]), sum(nums[(index_nums[0]+1):]), sum(nums))
#         new_list = []
#         for i in range(0,len(index_nums)-1):
#             for j in range(i+1,len(index_nums)):
#                 # print(i,j)
#                 if (index_nums[i ] - index_nums[j]) != 1:
#                     new_list.append(nums[(index_nums[i] + 1):(index_nums[j])])
#     # if
#             new_list.append(nums[(index_nums[i] + 1):])
#             new_list.append(nums[:index_nums[i]])
#         print(new_list)
#         max_list = []
#         for k in range(0,len(new_list)):
#             max_list.append(sum(new_list[k]))
#         print(max_list)
#         print(max(max_list))
#         print(new_list[max_list.index(max(max_list))])
#         return(max(max_list))
# mymethod 1
# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         onesum = 0
#         maxsum = nums[0]
#         for i in range(len(nums)):
#             onesum += nums[i]
#             maxsum = max(onesum, maxsum)
#             if onesum < 0:
#                 onesum = 0
#         return maxsum
# mymethod 2
class Solution:
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            subMax = max(nums[i] + nums[i-1], nums[i])
            nums[i] = subMax
        return max(nums)
nums = [-1,0,-2,2,3,4,5]
s = Solution()
print(s.maxSubArray(nums))
# print(sum(1,2,3))
