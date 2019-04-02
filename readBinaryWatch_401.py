class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num >= 9:
            return []
        if num == 0:
            return ['0:00']
        list1 = [8, 4, 2, 1]
        list2 = [32, 16, 8, 4, 2, 1]


