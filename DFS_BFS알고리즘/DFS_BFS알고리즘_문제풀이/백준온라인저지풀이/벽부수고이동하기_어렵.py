"""
N*M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 
1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 
이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 
이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 
벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

"""
import sys
from collections import deque
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
#3차원 행렬 선언
visited=[[[0]*2 for _ in range(m)]for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    queue=deque()
    queue.append([0,0,0])
    visited[0][0][0]=1
    while queue:
        x,y,z=queue.popleft()
        if x==(n-1) and y==(m-1):#만약 목적지에 도착하면 거기 값을 반환
            return visited[n-1][m-1][z]
        for i in range(4):#상하좌우 순서대로 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:#경계넘으면 continue
                continue
            if graph[nx][ny]==1 and z==0:#다음방향에 벽이 있고 벽을 부순적이 없는 경우
                queue.append([nx,ny,1])#마지막 값이 1이면 벽을 부순적이 있다는 것임
                visited[nx][ny][1]=visited[x][y][0]+1
                #[][][1]은 벽을 파괴한 이후 [][][0]은 파괴 이전
            if graph[nx][ny]==0 and visited[nx][ny][z]==0:
                queue.append([nx,ny,z])
                visited[nx][ny][z]=visited[x][y][z]+1
    return -1
        
print(bfs())