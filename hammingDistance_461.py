class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # res = bin(x)
        list_x = [int(i) for i in str(bin(x))[2:]]
        list_y = [int(i) for i in str(bin(y))[2:]]
        count = 0
        len_x = len(list_x)
        len_y = len(list_y)
        if len_x < len_y:
            count += sum(list_y[:(len_y - len_x)])
            res_xor = [list_y[(len_y - len_x):][i] + list_x[i] for i in range(len(list_x))]
            # res_xor = bin(y)[2+len_y - len_x] ^ bin(y)[2:]
        else:
            count += sum(list_x[:(len_x - len_y)])
            # res_xor = bin(x)[2 + len_x - len_y] ^ bin(x)[2:]
            res_xor = [list_x[(len_x - len_y):][i] + list_y[i] for i in range(len(list_y))]
        # res_xor = list_y ^ list_x
        print(bin(14 ^ 2))
        print(13 << 2)
        return count + res_xor.count(1)
s = Solution()
x = 14
y = 2
print(s.hammingDistance(x, y))