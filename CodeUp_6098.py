 # 10*10 크기의 미로 상자 구조와 먹이 위치 입력
ant_box = []
for i in range(10):
    ant_box.append(list(map(int,input().split())))

#Test_case
#ant_box = [ [1,1,1,1,1,1,1,1,1,1],
#           [1,0,0,1,0,0,0,0,0,1],
#           [1,0,0,1,1,1,0,0,0,1],
#           [1,0,0,0,0,0,0,1,0,1],
#           [1,0,0,0,0,0,0,1,0,1],
#           [1,0,0,0,0,1,0,1,0,1],
#           [1,0,0,0,0,1,2,1,0,1],
#           [1,0,0,0,0,1,0,0,0,1],
#           [1,0,0,0,0,0,0,0,0,1],
#           [1,1,1,1,1,1,1,1,1,1]]

x , y = 1 , 1
while (True):
    if ant_box[x][y] == 2:
        ant_box[x][y] = 9
        break
    elif ant_box[x+1][y] == 1 and ant_box[x][y+1] == 1:
        ant_box[x][y] = 9
        break

    ant_box[x][y] = 9

    if ant_box[x][y+1] == 1:
        x += 1
    elif ant_box[x+1][y] == 1:
        y += 1
    else:
        y += 1

for i2 in range(10):
    for j2 in range(10):
        print(ant_box[i2][j2],end=' ')
    print()
