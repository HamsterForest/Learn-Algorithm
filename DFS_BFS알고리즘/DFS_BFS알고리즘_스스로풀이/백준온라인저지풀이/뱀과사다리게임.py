"""
게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다. 
게임은 크기가 10*10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행된다. 
보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다. 
예를 들어, 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, 
i+4번 칸으로 이동해야 한다. 만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다. 
도착한 칸이 사다리면, 사다리를 타고 위로 올라간다. 뱀이 있는 칸에 도착하면, 
뱀을 따라서 내려가게 된다. 즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고, 
뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.

첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다. 
x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다. 
u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 
모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다. 
항상 100번 칸에 도착할 수 있는 입력만 주어진다.
"""
import sys
from collections import deque
n,m=map(int,input().split())#사다리 수, 뱀의 수
ladder_s=[0 for _ in range(n)]
ladder_f=[0 for _ in range(n)]
snake_s=[0 for _ in range(m)]
snake_f=[0 for _ in range(m)]
for i in range(n):
    ladder_s[i],ladder_f[i]=map(int,sys.stdin.readline().split())
for i in range(m):
    snake_s[i],snake_f[i]=map(int,sys.stdin.readline().split())


visited=[0 for _ in range(100)]

def bfs():
    queue=deque()
    queue.append(0)
    visited[0]=1
    while(queue):
        #print(queue)
        num=queue.popleft()
        for i in range(6):
            n=i+1
            if (num+n)<100:
                if visited[num+n]==0: 
                    if (num+n+1) in snake_s:
                        n_num=snake_f[snake_s.index(num+n+1)]-1
                        if visited[n_num]==0:
                            queue.append(n_num)
                            visited[n_num]=visited[num]+1
                        visited[num+n]=visited[num]+1
                    elif (num+n+1) in ladder_s:
                        n_num=ladder_f[ladder_s.index(num+n+1)]-1
                        if visited[n_num]==0:
                            queue.append(n_num)
                            visited[n_num]=visited[num]+1 
                        visited[num+n]=visited[num]+1 
                    else:
                        queue.append(num+n)
                        visited[num+n]=visited[num]+1    
            
       
bfs()
#print(visited)
print(visited[99]-1)