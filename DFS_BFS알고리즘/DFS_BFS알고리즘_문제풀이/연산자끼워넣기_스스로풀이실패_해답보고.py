"""
1. n개의 수로 이루어진 수열 a_1~a_n이 주어진다.
2. 수와 수 사이에 들어갈 n-1개의 연산자가 주어진다. 연산자는 + - * / 중하나
3. 들어갈 연산자의 종류별 수가 제한된다.
4. 이 때 최대값과 최소값을 구하는 알고리즘

나의 제안
1. for 문을 이용해 섞어질 수 있는 연산자 배열을 만든다.
예를들어 + 2개 - 1개 / 1개가 제한이라면, [0,0,2,3]
2. 1번의 모든 가능한 순서들을 저장한다.
3. 2를 토대로 모든 계산을 수행하고 그 결과 값을 저장한다.
4. 3값의 최대값과 최소값을 구한다.
못푼이유. 2번 구현을 못하겠다.

해답에서 dfs를 이용하여 해결하는 방법
0. + - * / 의 개수를 각각의 변수에 받는다.
1. 깊이 우선탐색의 재귀함수를 이용하여 모든경우의수를 한번에 계산한다.
1_1. 초기에 dfs함수는 i=1과 data[0]=a_1을 받는다. (1이 n과 같아지면 최대최소값 도출을 한다.)
1_2. 각 연산자들의 변수가 0이 될때까지 1씩 차감하며 재귀함수에 보낸다.
재귀함수에는 i+1과 a_1에 data[i]를 넣어준다.... 


"""
n= int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

max_val=-1e9
min_val=1e9

def dfs(i, now):
    global add,sub,mul,div,max_val,min_val
    if i==n:
        max_val=max(max_val,now)
        min_val=min(min_val,now)
    else:
        if add>0:
            add-=1
            dfs(i+1,now+data[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,now-data[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,now*data[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,int(now/data[i]))
            div+=1





dfs(1, data[0])
print(max_val, min_val)
        


    

