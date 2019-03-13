class Soultion():
    def shell_sort(self, nums):
        if len(nums) == 0:
            return None
        gap = len(nums)
        while gap > 1:
            gap = gap // 2
            for i in range(gap, len(nums)):
                for j in range(i%gap, i, gap):
                    if nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
        return nums
s = Soultion()
nums = [1,2,2,5,4,6,3,8,19,23,7]
print(s.shell_sort(nums))