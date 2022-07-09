"""
n*m크기의 금광이 있다. 금광은 1*1크기의 칸으로 나누어져 있으며, 각칸은 특정 크기의 금이 있다.
1. 채굴자는 첫 번째열부터 출발하여 금을 캐기 시작한다.
2. 첫 번째열의 어느 행에서든 출발할 수 있다.
3. 이후 m번에 걸쳐서 매번 오른쪽위, 오른쪽, 오른쪽아래 3가지 중 하나의 위치로 이동해야한다.
4. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램

첫째 줄. 테스트 케이스 t
매 테스트 케이스의 첫째줄. n과 m
매 테스트 케이스의 둘째줄. n*m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됨

-----------------------------------------------------------------------------------------
일단 든 생각은 bfs로도 풀 수 있지 않을까라는 생각이다.
모든 경우의수를 구하고 그에 대한 최대값을 출력하는 것이다.

다이나믹 프로그래밍을 이용해 만들때 가장 중요한 것은 점화식을 세우는 것이다.

금광의 왼쪽에서부터 차례로 채굴한다고 보자.


점화식
dp[i][j]=array[i][j]+max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])
"""
import sys

t=int(input())
#최종 결과값이 저장되는 곳
result=[0]*t

for x in range(t):
    array=[]#초기의 리스트
    dp=[]#1차원을 2차원으로 만들어 넣음
    
    n,m=map(int,sys.stdin.readline().split())
    array.extend(list(map(int,sys.stdin.readline().split())))

    #1차원 배열을 2차원으로 만드는 과정
    index=0
    for i in range(n):
        dp.append(array[index:index+m])
        index+=m

    #다이나믹 프로그래밍
    for j in range(1,m):#열
        for k in range(n):#행
            #왼쪽 위에서 오는 경우
            if k==0:
                left_up=0
            else:
                left_up=dp[k-1][j-1]
            #왼쪽 아래에서 오는 경우
            if k==n-1:
                left_down=0
            else:
                left_down=dp[k+1][j-1]
            #왼쪽에서 오는 경우
            left=dp[k][j-1]
            dp[k][j]=dp[k][j]+max(left_up,left_down,left)

    #최종 결과
    
    for i in range(n):
        result[x]=max(result[x],dp[i][m-1])



for y in range(t):
    print(result[y])