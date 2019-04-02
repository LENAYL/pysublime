import math
# import numpy as np
import sys
l = [200,0, 200, 10, 200, 50, 200, 30, 200, 25]
# s = sys.stdin.readline().strip()
# l = s.split(' ')
d = [[0,0]]
for i in range(5):
    temp = l[i*2: i*2+2]
    d.append(temp)
# dist = np.zeros((6,6))
dist = [[0,0,0,0,0,0,], [0,0,0,0,0,0,], [0,0,0,0,0,0,], [0,0,0,0,0,0,], [0,0,0,0,0,0,],[0,0,0,0,0,0,]]
for i in range(6):
    for j in range(6):
        a = (int(d[i][0])-int(d[j][0]))**2 + (int(d[i][1]) - int(d[j][1]))**2
        dist[i][j] = math.sqrt(a)
i = 1
n = 6
j = 0
sum_path = 0
s = []
s.append(0)
while True:
    k = 1
    Dtemp = 1000000
    while True:
        l = 0
        flag = 0
        if k in s:
            flag = 1
        if (flag == 0) and (dist[k][s[i-1]] < Dtemp):
            j = k
            Dtemp = dist[k][s[i-1]]
        k += 1
        if k >= n:
            break
    s.append(j)
    i += 1
    sum_path += Dtemp
    if i >= n:
        break
sum_path += dist[0][j]
print(int(sum_path))



