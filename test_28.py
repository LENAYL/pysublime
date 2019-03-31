# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        left = 0
        right = len(data) - 1
        first = self.getleft(data, k, left, right)
        end = self.getright(data, k, left, right)
        return end - first + 1

    def getleft(self, data, k, left, right):
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getright(self, data, k, left, right):
        while left <= right:
            mid = (left + right) // 2
            if data[mid] <= k:
                left = mid + 1
            else:
                right = mid - 1
        return right


a = Solution()
data = [3,3,3,3,4,5]
# data = ['1','2','3','3','4']
n = 3
print(a.GetNumberOfK(data, n))