class Soultion():
    def merge_sort(self, left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        res = res +left[i:] + right[j:]
        return res
    def main_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = self.main_sort(nums[:mid])
        right = self.main_sort(nums[mid:])
        return self.merge_sort(left, right)
s = Soultion()
nums = [1,2,6,4,2,4,3,9,4]
print(s.main_sort(nums))