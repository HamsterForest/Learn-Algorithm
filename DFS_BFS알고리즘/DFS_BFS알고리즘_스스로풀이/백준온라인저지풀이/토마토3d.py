"""
백준 7569
토마토문제로 전과 같다. 그러나 여기서 토마토는 3d로 배치되며
익은 토마토는 그 익음을 좌,우,앞,뒤,상,하로 전파한다.
"""
#안익은거->0 익은거->1 빈칸->-1
import sys
from collections import deque
m,n,h=map(int,input().split())#h는 높이
graph=[]#어떤 한 층의 창고
graph2=[]#전체적인 창고
#graph2에 3차원 리스트로 저장
for _ in range(h):
    for _ in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))
    graph2.append(graph)
    graph=[]
#익은 토마토는 어디?
r_t=[]
#안익은 토마토 수
gt=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph2[i][j][k]==1:
                r_t.append([i,j,k])
            if graph2[i][j][k]==0:
                gt+=1


#상하좌우 위 아래
dz=[0,0,0,0,-1,1]
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]

def bfs():
    global gt
    count=0#며칠 경과
    queue=deque()
    queue.extend(r_t)#익은 토마토가 있던 모든 위치를 큐에 넣는다.

    while queue:

        z,x,y=queue.popleft()

        for i in range(6):
            nz=z+dz[i]
            nx=x+dx[i]
            ny=y+dy[i]
            if nz<0 or nx<0 or ny<0 or nz>=h or nx>=n or ny>=m:
                continue
            if graph2[nz][nx][ny]==0:
                queue.append([nz,nx,ny])
                graph2[nz][nx][ny]=graph2[z][x][y]+1
                count=max(count,graph2[nz][nx][ny])
                gt-=1
    return count
    

if gt==0:
    print(0)
else:
    #안익은 토마토가 있는지 확인
    result=bfs()-1
    if gt==0:
        print(result)
    else:
        print(-1)