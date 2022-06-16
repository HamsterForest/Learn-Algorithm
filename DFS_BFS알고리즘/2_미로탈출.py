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
"""

from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네 방향을 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#bfs구현
def bfs(x,y):
    #큐 구현을 위해 deque사용
    queue=deque()
    queue.append((x,y))
    #큐가 빌때까지 반복
    while queue:
        x,y=queue.popleft()
        #현재위치에서 상하좌우의 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #벽(괴물)인경우 무시
            if graph[nx][ny]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))
    


