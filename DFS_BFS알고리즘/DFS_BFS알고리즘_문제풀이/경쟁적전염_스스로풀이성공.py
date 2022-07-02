"""
1. n*n크기의 시험관이 있다.
2. 특정한 위치에는 특정한 바이러스가 있다. 바이러스의 종류는 1~k
3. 모든 바이러스는 1초마다 상하좌우의 방향으로 증식한다.
4. 매초 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
5. 어떤 칸에 이미 바이러스강 있으면 다른 바이러스는 들어 갈 수 없다.
6. s초가 지난후 (x,y)에 존재하는 바이럿의 종류를 출력하는 프로그램
"""
n,k=map(int, input().split())

graph=[]
temp=[[0]*n for _ in range(n)]

for i in range(n):
   graph.append(list(map(int,input().split())))

print("s,x,y입력")

s,x,y=map(int,input().split())

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def infect(virus):#바이러스를 한번 감염 지금 딱 한번만 감염시키지 못하는 상황
    location=[]

    for i in range(n):
        for j in range(n):
            if graph[i][j]==virus:
                location.append([i,j])

    for data in location:
        
        print("감염중 : {0}".format(virus))
        print(graph)
        for k in range(4):
            nx=data[0]+dx[k]
            ny=data[1]+dy[k]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=virus




def select():
    for _ in range(s):#몇초동안 감염진행?
        for i in range(k):#순서대로 감염진행
            infect(i+1)

select()

print(graph)

result=graph[x-1][y-1]
print(result)