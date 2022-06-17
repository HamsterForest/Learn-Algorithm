"""
1. n*m크기의 얼음 틀이 있음.
2. 구멍이 있는 칸은 0 구멍이 막혀 있는 칸은 1로 표현된다.
3. 구멍이 뚫려있는 칸끼리 붙어 있는 경우 서로 연결되어 있는 것이라 간주함.
4. 이 때 얼음 틀에 물을 부었을 때 생성되는 얼음의 개수를 구하자.

여기서는 보지 않고 다시 해본다.
"""
n,m=map(int,input().split())
graph=[]
visited=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if graph[x][y]==1:
        return False
    if (x,y) in visited:
        return False
    visited.append((x,y))
    #상하좌우로 침입
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True

result=0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)
