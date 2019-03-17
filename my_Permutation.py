class Soultion():
    def my_Permutation(self,str):
        if len(str) == 0:
            return None
        res = []
        path = ''
        self.helper(str, res, path)
        return sorted(list(set(res)))
    def helper(self, str, res, path):
        if len(str) == 0:
            res.append(path)
        for i in range(len(str)):
            self.helper(str[:i] + str[i+1:], res, path + str[i])
s = Soultion()
str = 'abbc'
print(s.my_Permutation(str))