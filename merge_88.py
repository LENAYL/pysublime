class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # if len(nums1) < (m + n):
        #     return False
        # cout = 0
        # index = 0
        # for i in range(n):
        #     j = index
        #     if j < (m +cout):
        #         if nums1[j] < nums2[i]:
        #             j += 1
        #         else:
        #             nums1.insert(j, nums2[i])
        #             index = j
        #             cout += 1
        #             j = m + cout
        #     else:
        #         nums1[j:] = nums2[i:]
        # return nums1
        try:
            count = 0
            i = 0
            j = 0
            while i < n and j < (m + count):
                if nums1[j] < nums2[i]:
                    j += 1
                else:
                    nums1.insert(j, nums2[i])
                    i += 1
                    j += 1
                    count += 1
            else:
                if j >= (m+count):
                    nums1[j:] = nums2[i:]
                    nums1[:] = nums1[:(m+n)]
                    # nums1 = nums1[0:1]
                    # nums2 =
                    # return nums1
                else:
                    nums1[:] = nums1[:(m + n)]
                    # return nums1
        except:
            return False

s = Solution()
nums3 =  [2,0]
m = 1
nums4 = [1]
# nums1[0:]=nums2[1:]
# print(nums1)
n = 1
s.merge(nums3, m, nums4, n)
print(nums3)
# print(nums5)
# method 2
# nums1[m:(m+n)] = nums2[:n]
# nums1.sort()