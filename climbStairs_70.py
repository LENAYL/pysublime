# class Solution:
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         from itertools import combinations
#         count = 0
#         for i in range(0,(n//2) +1):
#             combins = [c for c in combinations(range(n -i), i)]
#             count += len(combins)
#         return count
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # from itertools import combinations
        # count = 0
        # for i in range(0,(n//2) +1):
        #     combins = [c for c in combinations(range(n-i), i)]
        #     count += len(combins)
        # return count
        nums = [0, 1, 2]
        for i in range(3, n+1):
            nums.append(nums[i-1] + nums[i-2])
        return nums[n]
s = Solution()
print(s.climbStairs(35))