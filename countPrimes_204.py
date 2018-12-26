class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i] == 1:
                prime[i * i:n:i] = [0] * len(prime[i * i:n:i])   # i 的倍数全部置0
        return sum(prime)


        # import math
        # dict = {1:1, 3: 3, 7:7, 9:9}
        # list = [2, 3, 5]
        # # count = 0
        # if n > 6:
        #     count = 3
        #     for i in range(7, n, 2):
        #         d = i %10
        #         if d in dict:
        #             for j in d:
        #                 if dict[j] < (i//2):
        #                     if i % dict[j] == 0:
        #                         break


                    # if (i % math.sqrt(i) != 0) and (i % 3 != 0):
                    #     count += 1

                # if i % 10 != 0:
                #     j = 0
                #     while j < len(list):
                #         if i % list[j] == 0:
                #             j = len(list)+10
                #         else:
                #             j += 1
                #     if j == len(list):
                #         count += 1

s = Solution()
n = 1000
print(s.countPrimes(n))


