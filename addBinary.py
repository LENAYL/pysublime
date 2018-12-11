class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a)
        b = int(b)
        sum_num = str(a + b)
        new_sum = ''
        temp = 0
        j = ''
        if int(sum_num) <= 1:
            return sum_num
        print(type(sum_num))
        for i in reversed(str(sum_num)):
            # print(type(i))
            print(i)
            j = str(int(i) + temp)
            if int(j) < 2:
                new_sum += j
                temp = 0
            else:
                new_sum += str(int(j)%2)
                temp = int(int(j)/2)
        # if new_sum[-1] == '0' and temp == 0:
        #     return '0'
        # else:
        #     new_sum += str(temp)
        if temp == 0:
            return new_sum[::-1]
        else:
            new_sum += str(temp)
        return new_sum[::-1]
s = Solution()
a = '100'
b = '110010'
print(s.addBinary(a,b))
# print(type(str(s.addBinary(a, b))))
# print(int(3/2))
# print(i for i in range(5,-1,0))
