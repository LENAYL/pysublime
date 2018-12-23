#
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # if numRows == 0:
        #     return False
        # g_list = []
        # # while numRows:
        # # t_list = []
        # for i in range(numRows):
        #     tem_list = []
        #     if 0 <= i < 2:
        #         while i+1:
        #             tem_list.append(1)
        #             i -= 1
        #         g_list.append(tem_list)
        #     else:
        #         t_list = g_list[i-1]
        #         for j in range(len(t_list)-1):
        #             tem_list.append(t_list[j] + t_list[j + 1])
        #         g_list.append([1]+ tem_list+ [1])
        # return g_list

        # 参考了答案版本
        result = []
        for i in range(numRows):
            now = [1]*(i+1)
            if i >= 2:
                for j in range(1,len(pre)):
                    now[j] = pre[j-1] + pre[j]
            result += [now]
            pre = now
        return result



s = Solution()
n = 5
print(s.generate(n))




