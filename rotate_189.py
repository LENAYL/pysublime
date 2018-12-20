class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #method 1
        # while k:
        #     nums.insert(0,nums.pop())
        #     k -= 1
        # return nums


        # method 2
        # nums[:] = nums[-k:] + nums[0:len(nums) - k]
        k = k%len(nums)
        l = len(nums[:-k])
        for i in nums[:-k]:
            nums.append(i)
        del nums[:l]
        return nums





s =Solution()
nums =[1,2,3,4,5,6,7]
# nums = [1]
k = 3
print(s.rotate(nums, k))