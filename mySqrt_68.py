# class Solution:
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         if x == 1:
#             return x
#         mid = int(x/2)
#         while mid < x:
#             # if (x / mid) == mid:
#             if mid * mid <= x < (mid+1) * (mid + 1):
#                 return mid
#                 break
#             elif (x / mid) > mid:
#                 l = mid
#                 r = x
#                 mid = int((l + r)/2)
            # continue
            # else:
            #     l = int(x / mid)
            #     r = mid
            #     mid = int((l + r) / 2)
            # continue
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)
s = Solution()
print(s.mySqrt(300))

