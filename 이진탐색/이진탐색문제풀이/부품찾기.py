"""
동빈이네 매장에는 부품이 n개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느날 손님이
m개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고
손님이 문의한 부품 m개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인 하는 프로그램을 작성해보자.

"""
import sys
n=int(input())
supply=[]
supply.extend(list(map(int,sys.stdin.readline().split())))
m=int(input())
require=[]
require.extend(list(map(int,sys.stdin.readline().split())))

#가지고 있는 부품을 정렬
supply.sort()
#이진탐색
def binary_search(target):
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if supply[mid]==target:
            return True
        elif supply[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return False

#고객이 원하는 부품을 하나씩 이진탐색을 돌린다.
result=[]
for i in require:
    if binary_search(i):
        result.append("yes")
    else:
        result.append("no")

for i in result:
    print(i,end=' ')
