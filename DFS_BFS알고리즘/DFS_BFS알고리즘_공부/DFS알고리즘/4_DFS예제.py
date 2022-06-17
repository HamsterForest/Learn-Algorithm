#dfs 메서드 정의
from re import T


def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v]=True
    print(v, end='')#end=''는 다음 print에서 자동 줄바꿈없이 출력하게 함
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph=[#인접 리스트 형식으로 그래프를 작성
    [],#노드0은 없음
    [2,3,8],#노드 1은 2,3,8과 연결
    [1,7],#노드 2는 1,7과 연결
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형을 표현 
visited=[False]*9

dfs(graph,1,visited)