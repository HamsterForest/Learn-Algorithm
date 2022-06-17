"""
1. n*m의 미로
2. 미로 안의 괴물을 피해 탈출 해야 함.
3. 처음 위치는 (1,1) 출구는(n,m)에 존재
4. 한번에 한 칸씩 이동 가능
5. 괴물이 있는 부분=0 괴물이 없는 부분=1
6. 미로는 반드시 탈출 가능 한 미로가 제시됨
7. 탈출을 위한 최소 칸 개수
8. 칸을 셀 때는 시작과 끝 칸을 포함
9. 시작칸과 마지막 칸은 항상 1임

여기서는 보지 않고 다시 해본다.
"""
from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#상하좌우
dx=(-1,1,0,0)
dy=(0,0,-1,1)

def bfs():
    
    queue=deque()
    queue.append((0,0))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]!=1:
                continue
            queue.append((nx,ny))
            graph[nx][ny]=graph[x][y]+1

bfs()
print(graph)
print(graph[n-1][m-1])

