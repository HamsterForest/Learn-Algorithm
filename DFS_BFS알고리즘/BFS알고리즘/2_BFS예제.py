from collections import deque
import queue

#bfs메서드 정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque라이브러리 사용
    queue=deque([start])
    #현재 노드를 방문 처리
    visited[start]=True
    #큐가 빌 때 까지 반복
    while queue:
        #큐에서 원소 하나를 빼서 출력
        v=queue.popleft()
        print(v,end='')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
           if not visited[i]:
                queue.append(i)
                visited[i]=True

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

#각 노드가 방문된 정보를 저장
visited=[False]*9

bfs(graph,1,visited)