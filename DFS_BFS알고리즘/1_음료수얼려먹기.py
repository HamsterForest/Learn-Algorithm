"""
1. n*m크기의 얼음 틀이 있음.
2. 구멍이 있는 칸은 0 구멍이 막혀 있는 칸은 1로 표현된다.
3. 구멍이 뚫려있는 칸끼리 붙어 있는 경우 서로 연결되어 있는 것이라 간주함.
4. 이 때 얼음 틀에 물을 부었을 때 생성되는 얼음의 개수를 구하자.
"""

#해결법
#1. 특정한  지점의 주변 상하좌우를 살펴본 뒤에 주변 지점중에서 값이 0이면서 아직 방문하지 않은곳이
#있으면 해당 지점을 방문
#2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 다시 진행하면 모든 지점을 방문 가능
#3. 1~2과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))#split을 안쓴건 두자리수가 들어갈 일이 없기 때문!!

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        #해당노드방문처리
        graph[x][y]=1
        #상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#모든 노드에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs수행
        if dfs(i,j)==True:
            result+=1

print(result)

