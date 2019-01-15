class NumArray(object):
    global sum_nums
    sum_nums = 0


    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # self.sum_nums = None
        self.sum_nums = [0]
        for i in nums:
            self.sum_nums.append(i + self.sum_nums[-1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_nums[j+1] - self.sum_nums[i]

# Your NumArray object will be instantiated and called as such:
nums = [-2,0,3,-5,2,-1]
obj = NumArray(nums)
i = 2
j = 5
param_1 = obj.sumRange(i,j)
print(param_1)