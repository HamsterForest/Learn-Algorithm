"""
체스판 위에 한 나이트가 놓여져 있다. (체스의 나이트와 같은 방식으로 이동)
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l * l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} * {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
"""
from collections import deque

#나이트 이동 경우의 수
dx=[-2,-2,-1,1,2, 2, 1,-1]
dy=[-1, 1, 2,2,1,-1,-2,-2]

def bfs():
    queue=deque()
    x,y=s
    queue.append([x,y])
    visited[x][y]=1
    while queue:
        x,y=queue.popleft()
       
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=l or ny>=l:
                continue
            if visited[nx][ny]==0:
                queue.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1

t=int(input())#테스트케이스의 수

result=[]

for _ in range(t):
    l=int(input())#체스판의 크기 가로=세로
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    x,y=f
    visited=[[0]*l for _ in range(l)]
    bfs()
    result.append(visited[x][y]-1)
    
for i in result:
    print(i)

