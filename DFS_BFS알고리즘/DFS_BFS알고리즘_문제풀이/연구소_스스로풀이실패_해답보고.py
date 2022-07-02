"""
컨셉 : 바이러스연구소에서 바이러스가 유출. 확산 막기위해 연구소에 벽을 세운다.
1. 연구소 크기는 n*m의 직사각형, 직사각형은 1*1의 정사각형으로 나누어져있음
2. 연구소는 빈칸과 벽으로 이루어지며 벽은 칸 하나를 가득 차지함.
3. 일부 칸은 바이러스가 존재.
4. 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있음.
5. 새로 세울 수 있는 벽의 개수는 3개이며 3개를 꼭 세워야함.
6. 0 : 빈칸 1 : 벽 2 : 바이러스
7. 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램
"""

#벽을 3개 세우는 모든 경우의수를 확인한다.
#벽을 3개 세운 그 공간을 복사한다.
#복사한 공간에 감염을 발생시키고 최대로 감염을 진행시킨다.
#최대감염 이후 빈공간의 개수를 세고 저장



n,m=map(int,input().split())

#연구소 어느 위치에 무엇이 있는지 그려진다.
graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

temp=[[0] * m for _ in range(n)] #n*m의 빈공간 생성-> 감염실험공간

result=0 #최종결과물

#상하좌우 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def infected(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if temp[nx][ny]==1 or temp[nx][ny]==2:
            continue
        temp[nx][ny]=2
        infected(nx,ny)

def score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    print(temp)
    print("위에꺼 빈칸수 {0}".format(score))
    return score

def wall(count):
    global result
    if count==3:
        #temp에 graph 복사
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]
        #감염확인 함수
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    infected(i,j)
        #최종결과물에 비견할 빈칸수면 result에 저장
        result=max(result,score())
        return

    #차례로 모든 벽설치 경우의수
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1#빈공간이면 벽설치
                count+=1
                wall(count)#dfs의 초석
                count-=1
                graph[i][j]=0#벽 해체

      
wall(0)
print(result)


