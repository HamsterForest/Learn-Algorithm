"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.
"""
from collections import deque
n,m,v=map(int,input().split())
graph=[]

for _ in range(m):
    graph.append(list(map(int,input().split())))


def dfs(v):
    visited[v]=True
    print(v,end=' ')
    close=[]
    for i in graph:
        if v in i:
            if i[0]==v:
                if visited[i[1]]==False:
                    close.append(i[1])
            else:
                if visited[i[0]]==False:
                    close.append(i[0])
    if len(close)==0:
        return
    dfs(min(close))
    

def bfs(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        a=queue.popleft()

        print(a,end=' ')
        close=[]
        for i in graph:
         if a in i:
                if i[0]==a:
                    if visited[i[1]]==False:
                        close.append(i[1])
                        visited[i[1]]=True
                else:
                    if visited[i[0]]==False:
                        close.append(i[0])
                        visited[i[0]]=True
        if len(close)==0:
            continue
        close.sort()
        for i in range(len(close)):
            queue.append(close[i])
    


visited=[False]*(n+1)
dfs(v)
print("\n",end='')
visited=[False]*(n+1)
bfs(v)