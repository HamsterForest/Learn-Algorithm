"""
1. 1~n번 까지의 도시가 있다.
2. m개의 단방향 도로가 있다.
3. 모든 도로의 거리는 1이다.
4. 특정 도시 x에서 출발하여 도달 할 수 있는 도시중 최단 거리가 정확히 k인 모든 도시의 번호를 출력

"""

#도시개수 n, 도로개수 m, 최단거리조건 k, 출발도시번호 x
from collections import deque
from types import CoroutineType

n,m,k,x=map(int,input().split())
graph=[]
for i in range(m):
    graph.append(list(map(int,input().split())))

cities=[]
for i in range(n):
    cities.append([i+1,-1])#도시 종류들을 저장한다. 나중에 지어나갈 때 쓴다.
    #-1은 k값의 초기값(아직 k 값이 결정 되지 않음)


def bfs(x):
    count=0#k값이 되는것이 목표
    queue=deque()
    queue.append(x)
    cities[x-1][1]=0
    while queue:
        if count==k:
            break
        city=queue.popleft()
        count+=1
        for n in graph:
            if city == n[0]:#여기서는 그래프에서 city에서 이동할 수 있는 도시를 골라냄
                queue.append(n[1])#city에 연결되어 있는 도시
                if cities[n[1]-1][1]==-1:
                    cities[n[1]-1][1]=count
                               
bfs(x)

collected=[]

for result in cities:
    if result[1]==k:
        collected.append(result[0])

print(cities)

if collected:
    collected.sort()
    for i in range(len(collected)):
        print(collected[i])
else:
    print(-1)

