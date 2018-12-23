class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # method2
        res = 0
        count = 0
        while n:
            res = res*2 +n%2
            n = n//2
            count += 1
        while count < 32:
            res = res*2
            count += 1
        return res

        # method1 慢慢慢
        # res = ''
        # while n:
        #     rem = n % 2
        #     n = n//2
        #     res = res +''.join(str(rem))
        #     l = len(res)
        # if l < 32:
        #     for i in range(32-l):
        #         res = res + ''.join('0')
        #     # res[:] = res +[0]*(32 - l)
        # print(len(res))
        # print(res)
        # return int(res, 2)

s = Solution()
n = 15
print(s.reverseBits(n))

