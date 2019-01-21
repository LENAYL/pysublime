class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        m = "0123456789abcdef"
        res = ''
        for i in range(8):
            t = num & 15
            num = num >> 4
            res = m[t] + res
        return res.lstrip("0")


        # dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        # dict_2 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13,  'e': 14, 'f': 15}
        #
        # # hex_list = [16**7, 16**6, 16**5, 16**4, 16**3, 16**2, 16**1, 1]
        # hex_list =[1, 16 ** 1, 16 ** 2, 16 ** 3, 16 ** 4, 16 ** 5, 16 ** 6, 16 ** 7]
        # res_list = [0]*8
        # if num >= 0:
        #     flag = 0
        # else:
        #     flag = 1
        # num = abs(num)
        # if num > 16**8 or num < -16**8:
        #     return False
        # # i = 7
        # while num:
        #     for i in range (len(hex_list)-1):
        #         if hex_list[i] <= num < hex_list[i+1]:
        #             n = num//hex_list[i]
        #             res_list[7 - i] = dict[n][-1]
        #             num -= n * hex_list[i]
        #             break
        #     if num >= hex_list[-1]:
        #         n = num // hex_list[-1]
        #         res_list[0] = dict[n]
        #         num -= n * hex_list[-1]
        # # print(res_list)
        # if flag == 0:
        #     for i in range(len(res_list)):
        #         if res_list[i] == 0:
        #             # del res_list[i]
        #             pass
        #         else:
        #             res_list[:] = res_list[i:]
        #             break
        #     return ''.join('%s' % i for i in res_list)
        # else:
        #     for i in range(len(res_list)):
        #         if type(res_list[i]) is int:
        #             res_list[i] = 15 - res_list[i]
        #         else:
        #             res_list[i] = 15 - dict_2[res_list[i]]
        #     if type(res_list[-1]) is int:
        #         res_list[-1] += 1
        #     else:
        #         res_list[-1] = dict_2[res_list[-1]] + 1
        #     for i in range(len(res_list)-1, 0, -1):
        #         if res_list[i] == 16:
        #             res_list[i] = 0
        #             res_list[i - 1] += 1
        #             # res_list[i-1] = dict[dict_2[str(res_list[i-1])] +1]
        #     print(res_list)
        #     return ''.join(dict[int(i)] for i in res_list)







s = Solution()
num = 33
print(s.toHex(num))


