d, b = [], []
for i in range(19):
    d.append(list(map(int,input().split())))

a = int(input())
for a1 in range(a):
    b.append(list(map(int,input().split())))


for b1 in b:
    for i in range(19):
        if d[b1[0]-1][i] == 0:
            d[b1[0]-1][i] = 1
        else:
            d[b1[0]-1][i] = 0
        
        if d[i][b1[1]-1] == 0:
            d[i][b1[1]-1] = 1
        else:
            d[i][b1[1]-1] = 0

for i2 in range(19):
    for j2 in range(19):
        print(d[i2][j2],end=' ')
    print()