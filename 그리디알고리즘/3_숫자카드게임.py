"""
숫자카드는 n*m으로 배열 되어있음.
1. 먼저 뽑고자 하는 행을 선택.
2. 그 행에서 가장 작은 수를 선택.
이 과정에서 가장 큰 수를 뽑을 수 있도록 해야함. 그 행을 찾는 알고리즘
"""
#해결법
#1. 행 단위로 수를 입력 받는다.
#2. 그 행에서 가장 작은 수를 저장한다.
#3. 모든 행을 입력받으면, 2번에서 가장 큰수를 가지는 행을 출력한다.


n,m=map(int,input().split())
small=0
result=0

for i in range(n):
    data=list(map(int,input().split()))
    data.sort()
    print(data)
    if data[0]>small:
        small=data[0]
        result=i+1
        print(result)

print(result)
