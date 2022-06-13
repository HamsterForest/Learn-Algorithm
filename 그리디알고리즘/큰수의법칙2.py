"""
첫 번째보다 효율적인 알고리즘
이 문제에서 큰 수의 법칙은 가장큰수를 k번 더하고 두번째로 큰수를 1번 더하는 것을 반복한다.
따라서 이는 수열의 형태를 이룬다. 따라서 가장 큰 수를 몇번 더할지 계산 할 수 있다.
"""
import time
from turtle import end_fill

n,m,k=map(int, input().split())#파이썬에서 여러 데이터를 한번에 입력 받는 방법

data=list(map(int,input().split()))

start_time=time.time()

data.sort()#입력 받은 리스트를 정렬

first=data[n-1]#가장 큰 수
second=data[n-2]#두번째로 큰 수

#가장 큰 수가 더해지는 횟수
count=m//(k+1)*k
count+=m%(k+1)

result=first*count+second*(m-count)

print(result)

end_time=time.time()
print(end_time-start_time)