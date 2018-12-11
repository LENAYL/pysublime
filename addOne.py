a = [1, 2, 3]
sum = 0
for i in a:
    sum = sum*10 + i
sum += 1
print(list(int(j) for j in (str(sum))))
print(type(''.join(str(i) for i in a)))
print (type((int(''.join(str(i) for i in a)) + 1)))
print(str((int(''.join(str(i) for i in a)) + 1)))
print([int(i) for i in str((int(''.join(str(i) for i in a)) + 1))])
