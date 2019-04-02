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