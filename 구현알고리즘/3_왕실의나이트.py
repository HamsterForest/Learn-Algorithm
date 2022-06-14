"""
1. 8*8 체스판이 있다.
2. 나이트(말) 유닛이 어떤 좌표에 있을 때 그 유닛이 이동 할 수 있는 위치 수를 출력
3. x축은 a~h y축은 1~8로 입력받는다.
"""


locate=input()

x_str=locate[0]
y=int(locate[1])
x=0

x_str_list=["a","b","c","d","e","f","g","h"]

count=0

for idx, data in enumerate(x_str_list):
    if x_str==data:
        x=idx+1

steps=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

for step in steps:
    if x+step[0]>=1 and y+step[1]>=1 and x+step[0]<=8 and y+step[1]<=8:
        count+=1

print(count)
