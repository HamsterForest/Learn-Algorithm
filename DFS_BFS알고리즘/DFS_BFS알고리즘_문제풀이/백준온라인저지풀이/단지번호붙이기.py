"""
백준 2667
정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 
출력하는 프로그램을 작성하시오.
"""
from collections import deque

n=int(input())#지도의 크기 n*n
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    count=1#어떤 단지 안 집의 수
    queue=deque()
    queue.append([x,y])
    graph[x][y]=0#이미 확인한 집은 그래프에서 지움
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]!=0:
                queue.append([nx,ny])
                graph[nx][ny]=0
                count+=1
    return count
        
    

#지도 탐색
result=0#단지의 수
houses=[]#어떤 단지 안 집의 수

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            result+=1
            houses.append(bfs(i,j))

houses.sort()

print(result)
for data in houses:
    print(data)