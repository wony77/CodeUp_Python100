# 격자 판 가로 세로 받아서 테이블 만들기
box = list(map(int,input().split()))
table = [[0]*box[1] for i in range(box[0])]

# 막대의 갯수 받기
n = int(input())

# 막대의 갯수만큼 막대의 길이 방향 x , y 좌표 받기
stick = []
for i in range(n):
    stick.append(list(map(int,input().split())))

# 막대 받은것으로 테이블에 막대 놓는 방법
for stick1 in stick:
    if stick1[1] == 0:
        for i in range(stick1[0]):
            table[stick1[2]-1][stick1[3]-1+i] = 1
    else:
        for i in range(stick1[0]):
            table[stick1[2]-1+i][stick1[3]-1] = 1

# 테이블 출력
for i2 in range(box[0]):
    for j2 in range(box[1]):
        print(table[i2][j2],end=' ')
    print()