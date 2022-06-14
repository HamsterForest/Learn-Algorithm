"""
1. 여행가 n*n크기의 정사각형 공간에 있음 (1,1)~(n,n)
2. 여행가의 이동에 관한 계획서가 주어짐
L : 왼쪽 한 칸
R : 오른쪽 한 칸
U : 위로 한 칸
D : 아래로 한 칸
3. 정해진 공간 바깥으로의 이동은 무시됨.
4. 출발지점은 (1,1)
5. 도착할 지점의 좌표를 도출하는 알고리즘
"""

n=int(input())
plans=input().split()

plan_str=["L","R","U","D"]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

result_x=1
result_y=1

for plan in plans:
    for i in range(len(plan_str)):
        if plan==plan_str[i]:
            if result_x+dx[i]>=1 and result_y+dy[i]>=1 and result_x+dx[i]<=n and result_y+dy[i]<=n:
                result_x+=dx[i]
                result_y+=dy[i]

print(result_y, result_x)

        

