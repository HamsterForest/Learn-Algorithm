"""
1. n*m크기의 얼음 틀이 있음.
2. 구멍이 있는 칸은 0 구멍이 막혀 있는 칸은 1로 표현된다.
3. 구멍이 뚫려있는 칸끼리 붙어 있는 경우 서로 연결되어 있는 것이라 간주함.
4. 이 때 얼음 틀에 물을 부었을 때 생성되는 얼음의 개수를 구하자.

여기서는 보지 않고 다시 해본다.
"""
from collections import deque

n,m=map(int,input().split())
graph=[]
visited=[]
for i in range(n):
    graph.append(list(map(int,input())))

#상하좌우 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    if graph[x][y]==1:
        return False
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if graph[x][y]==1:
            continue
        graph[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==1:
                continue
            queue.append((nx,ny))
    return True


result=0

for i in range(n):
    for j in range(m):
        if bfs(i,j)==True:
            result+=1

print(result)
