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


n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

visited=[]
result=[]

def dfs(x,y,i):
    #현재 지점이 가능한 지점인지 알아보고 아니면 그냥 넘어가자
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if graph[x][y]==0:
        return False
    if (x,y) in visited:
        return False
    visited.append((x,y))
    result.append(i)
    graph[x][y]+=1
    #상하좌우를 살펴보며 가능한 지점이 있는지 알아보고 있으면 재귀함수로 들어가자
    dfs(x-1,y,i+1)#상
    dfs(x+1,y,i+1)#하
    dfs(x,y-1,i+1)#좌
    dfs(x,y+1,i+1)#우
    
    
    

dfs(0,0,1)
print(result)
print(max(result))


