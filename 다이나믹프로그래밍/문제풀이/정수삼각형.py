"""
    7
   3 8
  8 1 0
 2 7 4 4
4 5 2 6 5
위는 크기가 5인 정수삼각형의 한 모습이다.
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올때
선택된 수의 합이 최대가 되는 값을 구하는 프로그램을 작성하시오.

삼각형크기는 1~500이하
정수의 범위는 0~9999이하

내가 생각해본 점화식
a_(i,j)=max(a_(i-1,j-1),a_(i-1,j))+a_(i,j)
"""
import sys
n=int(input())#삼각형크기
graph=[]#dp테이블의 역할도 같이한다.

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(i+1):
        if j>0 and j<i:
            graph[i][j]=max(graph[i-1][j-1],graph[i-1][j])+graph[i][j]
        if j==0:
            graph[i][j]=graph[i-1][j]+graph[i][j]
        if j==i:
            graph[i][j]=graph[i-1][j-1]+graph[i][j]

result=max(graph[n-1])
print(result)