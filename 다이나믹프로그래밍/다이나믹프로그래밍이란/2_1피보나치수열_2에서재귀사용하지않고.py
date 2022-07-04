"""
재귀를 사용하면 오버헤드를 발생 할 수 있으므로 반복문을 사용하여 구현하면 다음과 같다.
재귀처럼 top-down이 아닌 bottom-up방식으로 한다.
"""
#이미 계산한 값을 저장하는 리스트를 선언
d=[0]*100
d[1]=1
d[2]=1

def fibo(x):
    for i in range(3,x+1):
        d[i]=d[i-1]+d[i-2]
    return d[x]


print(fibo(99))