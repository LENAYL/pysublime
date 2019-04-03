# -*- coding:utf-8 -*-
# class Solution:
#     # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
#     # 函数返回True/False
#     def duplicate(self, numbers, duplication):
#         # write code here
#         if len(numbers) == 0:
#             return False
#         n = len(numbers)
#         for i in range(len(numbers)):
#             index = numbers[i]
#             if index >= n:
#                 index -= n
#             if numbers[index] >= n:
#                 duplication[0] = index
#                 return True
#             numbers[index] += n
#         return False
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) == 0:
            return False
        n = len(numbers)
        for i in range(len(numbers)):
            if numbers[i] >= n or numbers[i] < 0:
                return False
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
                # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
        return False
s = Solution()
num = [2,1,3,1,4]
d = [0]
print(s.duplicate(num, d))
