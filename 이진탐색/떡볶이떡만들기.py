"""
동빈이네 떡볶이의 떡은 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총길이는
절단기로 잘라서 맞춰준다.
절단기에 높이 h를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 h보다 긴 떡은 h위읩 분이 잘릴
것이고, 낮은 떡은 잘리지 않는다.
예를들어 높이가 19,14,10,17인 떡이 나란히 있고 h=15라고 하면, 자른뒤의 높이는
15,14,10,15가 된다. 잘린 떡의 길이는 4,0,0,2이다. 손님은 6cm 만큼의 길이를 가져간다.
손님이 왔을 때 요청한 총 길이가 m일 때 적어도 m만큼의 떡을 얻기 위해 절단기에 설정할 수 있는
높이의 최대 값을 구하는 프로그램을 작성하시오.

첫째 줄에 떡의 개수n과 요청한 떡의 길이m이 주어진다.
둘째 줄에 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 m이상이므로 손님은 필요한 양만큼
떡을 사갈 수 있다. 
"""
#파라메트릭 서치 문제-이진탐색을 이용해 적절한 h값을 찾는다.

import sys
n,m=map(int,input().split())
array=[]
array.extend(list(map(int,sys.stdin.readline().split())))
big=max(array)
def binary_search():
    start=0
    end=big
    while start<=end:
        result=0
        mid=(start+end)//2
        for i in array:
            if (i-mid)>=0:
                result+=(i-mid)
        if result==m:
            return mid
        elif result>=m:
            start=mid+1
        else:
            end=mid-1
        
print(binary_search())