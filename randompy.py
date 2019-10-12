n = int(input())

ls = list(range(1, n + 1))

from random import shuffle

shuffle(ls)

m = int(input())

for i in range(m):
    print(ls[i % n])
