"""
1. n에서 1을 뺀다.
2. n을 k로 나눈다.
n과 k가 주어진다.
n이 1이 될때까지 1과 2를 수행하고 최소 횟수가 되어야한다.
n을 1로 만드는 알고리즘을 만들자.
"""
#해결법
#횟수가 적어지기 위해서는 2번과정이 최대로 이루어져야한다.
#k로 나누어질때까지 1을 계속 빼는 형식이 되면 된다.

n,k = map(int,input().split())
result=0

while 1:
    if n==1:
        break
    if n%k==0:
        n/=k
        result+=1
    else:
        n-=1
        result+=1

print(result)