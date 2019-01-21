class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res_list = [str(i) for i in range(1, n+1)]
        print(res_list)
        res_list[2: n: 3] = ['Fizz']*(n//3)
        res_list[4: n: 5] = ['Buzz']*(n//5)
        res_list[14: n : 15] = ['FizzBuzz']*(n//15)
        print(res_list)
s = Solution()
n = 60
print(s.fizzBuzz(n))