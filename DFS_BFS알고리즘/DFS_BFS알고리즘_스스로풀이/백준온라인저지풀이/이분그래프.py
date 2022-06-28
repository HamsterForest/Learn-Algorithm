"""
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 
분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 
순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 
각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 
"""
from collections import deque
import sys
k=int(input())#테스트케이스의 수

def bfs(graph,visited,start):
    queue=deque()
    queue.append(start)
    visited[start]=1#첫번째를 1로 색칠한다.
    while queue:
        num=queue.popleft()
        for i in graph[num]:#1과 연결되어 있는 노드들을 차례로 큐에 넣어야한다.
            if visited[i]==0:#만약 한번도 방문한적이 없는 노드라면
                queue.append(i)#큐에 넣는다.
                visited[i]=visited[num]*(-1)#전과 다른 색을 칠한다.
            elif visited[i]==visited[num]:#방문한적이 있는 노드인데, 색이 전과 이미 같다면(이분그래프아님)
                return False
    return True#한번도false반환이 없으면 이는 이분그래프
    
        
for _ in range(k):#테스트케이스별로 시험하기위한
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):#그래프 노드별로 묶기
        a,b=map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    visited=[0 for _ in range(v+1)]#여기에 각 노드별로 무슨색으로 칠해졌는지 저장됨
    for start in range(1,v+1):#그래프가 서로 연결되지 않을 경우를 고려해서 모든 노드에 대하여 검사
        if visited[start]==0:
            result=1
            result=bfs(graph,visited,start)*result#모든 노드를 검사중 하나라도false가나오면 false
            if result==0:
                break
    if result==1:
        print("YES")
    else:
        print("NO")
        
