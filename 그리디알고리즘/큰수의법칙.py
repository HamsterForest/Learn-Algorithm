"""
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰 수를 만드는 것이 목적이다.
단, 배열의 특정 인덱스에 해당하는 수는 연속해서는 k번만 더해 질 수 있다. 
ex) list=[2,4,5,4,6] m=8, k=3, => 6+6+6+5+6+6+6+5
"""
import time

#이를 해결하는 방법은 큰수를 k가 허용하는 만큼연속해서 더하고 그 다음으로 두번째로 큰수를 한번 더한 후
#다시 가장 큰수를 k가 허용하는 만큼 연속해서 더하는 것이다.


n,m,k=map(int, input().split())#파이썬에서 여러 데이터를 한번에 입력 받는 방법

data=list(map(int,input().split()))

start_time=time.time()

data.sort()#입력 받은 리스트를 정렬
first=data[n-1]#가장 큰 수
second=data[n-2]#두번째로 큰 수

result =0

while 1:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

print(result)

end_time=time.time()
print(end_time-start_time)

