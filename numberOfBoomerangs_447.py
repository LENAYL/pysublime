class Solution:
    def numberOfBoomerangs(self, points: 'List[List[int]]') -> 'int':
        # import math
        # import numpy as np
        res = 0
        for i in points:
            dict = {}
            for j in points:
                dis = (i[0] - j[0])**2 + (i[1] - j[1])**2
                if dis in dict:
                    dict[dis] += 1
                else:
                    dict[dis] = 1
            for k in dict.values():
                if k >=2:
                    res += k * (k - 1)
        return res

        # disatance = []
        # temp_1 = [0]*len(points)
        # temp_2 = [0]*len(points)
        # dict_i = {}
        # dict_j = {}
        # for i in range(len(points) - 1):
        #     # dict[i] = []
        #     for j in range(i+1,len(points)):
        #         disatance = np.sqrt(np.sum(np.square(i - j)))
        #         if disatance in dict_i:
        #             dict_i[disatance] += 1
        #
        #         else:
        #             dict_i[disatance] = 1
        #         dict_j[disatance] = 1
        #
        #         dict[i].append(np.sqrt(np.sum(np.square(i - j))))
                # disatance.append(np.sqrt(np.sum(np.square(i - j))))

