"""
백준 7576
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 
익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 
왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 
토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. 
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 
둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

시간초과 됨 bfs를 사용하지 않음 =>이게 문제일 수 있음
"""
#안익은거->0 익은거->1 빈칸->-1
import sys
from collections import deque
m,n=map(int,input().split())
graph=[]#창고
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
#안 익은 토마토의 수
rt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            rt+=1

#해당 칸 방문여부
visited=[[False]*m for _ in range(n)]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def tomato(x,y):
    visited[x][y]=True
    count=0#이번에 익힌 토마토의 수
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if visited[nx][ny]==True:
            continue
        if graph[nx][ny]==0:
            graph[nx][ny]=1#토마토가 익음
            visited[nx][ny]=True
            count+=1
    return count
    
#익은 토마토가 여러군데 분포되어 있을 경우 이들이 동시에 주변에 영향을 미쳐야한다.

f_break=False
result=0
tem=0
fail=False
while 1:
    if rt==0:#토마토 전부 익음
        break
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and visited[i][j]==False:
                tem+=tomato(i,j)
     
    visited=[[False]*m for _ in range(n)]#방문처 초기화
    result+=1
    if tem==0:#더이상 익힐 토마토가 없음
        fail=True
        break
    rt-=tem
    tem=0
    
        
if fail==True:
    print(-1)
else:
    print(result)
