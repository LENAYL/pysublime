# # -*- coding:utf-8 -*-
# # -*- coding:utf-8 -*-
# class Solution:
#     def GetNumberOfK(self, data, k):
#         # write code here
#         left = 0
#         right = len(data) - 1
#         first = self.getleft(data, k, left, right)
#         end = self.getright(data, k, left, right)
#         return end - first + 1
#
#     def getleft(self, data, k, left, right):
#         while left <= right:
#             mid = (left + right) // 2
#             if data[mid] < k:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return left
#
#     def getright(self, data, k, left, right):
#         while left <= right:
#             mid = (left + right) // 2
#             if data[mid] <= k:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return right
#
#
# a = Solution()
# data = [3,3,3,3,4,5]
# # data = ['1','2','3','3','4']
# n = 3
# print(a.GetNumberOfK(data, n))
# import math
#
# f = 11.2
# print (int(math.ceil(f))) #向上取整)
# print math.floor(f) #向下取整
# print round(f) #四
# str1 = 'abcdefg'
# s = ''
# s = str1[2:] + str1[:2]
# print(s)
# l = [1, 2, 3, 4]
# s = '.'.join(str(i) for i in l)
# print(type(s))
# a = -2
# print('a %s'% (bin(a)))
# print(bin(a&0xffffffff))
# print(bin(~a))
# b = 2
# print('b %s' % (bin(b)))
# l = 'abd'
# print(list(l))
# l = []
# d = {'2': 2, '3': 3}
# l.append(d)
# # d = {}
# # print(l)
# # d = {}
# class Solution():
#     def main(self, word, num, dictWords):
#         temp = []
#         for i in dictWords:
#             s = list(i)
#             dict = {}
#             for j in s:
#                 if j in dict:
#                     dict[j] += 1
#                 else:
#                     dict[j] = 1
#             temp.append(dict)
#         help_dict = {}
#         for i in word:
#             if i in help_dict:
#                 help_dict[i] += 1
#             else:
#                 help_dict[i] = 1
#         flag = False
#         res = []
#         for i in range(len(temp)):
#             for j in temp[i]:
#                 if j in help_dict and temp[i][j] <= help_dict[j]:
#                     flag = True
#                 else:
#                     flag = False
#                     break
#             if flag:
#                 res.append(dictWords[i])
#         return res
# s = Solution()
# word = 'rocksock'
# num = 4
# d = ['rocs', 'cksok', 'roky', 'sockro']
# print(s.main(word, num, d))
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        temp = [i for i in data]
        # temp = [0]*len(data)
        return self.mergeSort(temp, data, 0, len(data) - 1) % 1000000007

    def mergeSort(self, temp, data, low, high):
        if low >= high:
            temp[low] = data[low]
            return 0
        mid = (low + high) // 2
        left = self.mergeSort(data, temp, low, mid)
        right = self.mergeSort(data, temp, mid + 1, high)

        count = 0
        i = low   #  左边子序列的第一个数字
        j = mid + 1    #右边子序列的第一个数字
        index = low
        while i <= mid and j <= high:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]    # 排序
                count += mid - i + 1    #  左边子序列中从i个数字开始以后的都大于右边子序列的data[j]
                j += 1    #  j向后挪一个
            index += 1     # temp 数组向后挪
        while i <= mid:     #右边子序列遍历结束 剩余的左边子序列是已经排好序的，直接存入temp数组
            temp[index] = data[i]
            i += 1
            index += 1
        while j <= high:    # 同上
            temp[index] = data[j]
            j += 1
            index += 1
        return count + left + right
s = Solution()
num = [7,5,6,4]
print(s.InversePairs(num))