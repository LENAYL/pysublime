class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #  method 2
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        nums1.sort()
        nums2.sort()
        l1  = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        new_list = []
        while (i != l1) and j != l2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                new_list.append(nums1[i])
                i += 1
                j += 1
        return new_list
        # method 1
        # l1 = len(nums1)
        # l2 = len(nums2)
        # new_list = []
        # if l1 > l2:
        #     for i in nums2:
        #         if i in nums1:
        #             new_list.append(nums1.pop(nums1.index(i)))
        # else:
        #     for i in nums1:
        #         if i in nums2:
        #             new_list.append(nums2.pop(nums2.index(i)))
        # return new_list
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # l1 = len(nums1)
        # l2 = len(nums2)
        # new_list = []
        # if l1 > l2:
        #     for i in nums1:
        #         if i in nums2:
        #             new_list.append(i)
        # else:
        #     for i in nums2:
        #         if i in nums1:
        #             new_list.append(i)
        # return new_list


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersection(nums1, nums2))

