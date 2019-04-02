class Soultion():
    def select_sort(self, nums):
        if len(nums) == 0:
            return None
        for i in range(len(nums)-1):
            min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            if min != i:
                nums[min], nums[i] = nums[i], nums[min]
        return nums
s = Soultion()
nums = [1,2,6,4,2,4,3,9,4]
print(s.select_sort(nums))