a = int(input())
c = []
d = [[0]*19 for i in range(19)]
for i in range(a):
    b = input().split()
    b = list(map(int,b))
    c.append(b)

for c1 in c:
    d[c1[0]-1][c1[1]-1] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j],end=' ')
    print()