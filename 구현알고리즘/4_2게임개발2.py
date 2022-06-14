"""
1. 캐릭터가 맵안에서 움직이는 알고리즘
2. 맵의 크기는 정사각형 n*m
3. 맵의 각 칸은 (1,1)~(n,m)
4. 맵은 육지와 바다가 있으며, 육지는 0 바다는 1로 표시된다.
5. 현재위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈곳을 정함
6. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전 후
왼쪽으로 한 칸 이동하며, 만약 가보지 않은 칸이 없다면, 왼쪽으로 횐전만 하고 5번으로 돌아간다.
7. 만약 모든 방향이 이미 가본 칸이거나 바다인 칸인 경우, 바라보는 방향을 유지한 채로 한 칸
뒤로 가고 1단계로 돌아간다. 이 때 뒤쪽 방향이 이미 바다인 칸인 경우 움직임을 멈춘다.
8. 캐릭터가 방문한 칸의 수를 출력한다.
9. 처음 캐릭터가 위치한 칸은 항상 육지이다.

"""
#해설을 참조해서 다시만든것. 4_1이 너무 난잡하고 복잡해보여서


n,m =map(int,input().split())
x,y,c_dir=map(int,input().split())

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

#방향정리 북,동,남,서
#열
dy=[0,1,0,-1]
#행
dx=[-1,0,1,0]

def turnleft():# 서->남->동->북->서->남->동->북 계속 순환 할 수 있게 해 줌
    global c_dir
    c_dir-=1
    if c_dir==-1:
        c_dir=3

turn_count=0#4회전하면, 사방으로 0인지점이 없다는 것임, 그리고 처음 바라보던 방향 그것을 알기 위함
result=0#도출할 결과=>이동한 횟수

while 1:
    #현재 위치를 지도에 기록 지도=array
    array[x][y]=2 # 0 육지 1 바다 2 이미 다녀감
    #반시계방향으로 회전
    turnleft()
    turn_count+=1
    #현재 보고 있는 방향이 갈 수 있는지 확인 그리고 이동
    nx=x+dx[c_dir]#보고 있는 방향의 좌표, 행
    ny=y+dy[c_dir]#열
    if array[nx][ny]==0:
        x=nx
        y=ny
        result+=1
        turn_count=0
    if turn_count==4:#두가지 경우의수 뒷방향이 육지인가 아님 바다인가.
        turn_count=0
        nx=x-dx[c_dir]
        ny=y-dy[c_dir]
        if array[nx][ny]==1:
            break
        else:
            x=nx
            y=ny
            result+=1
    #print(x,y,c_dir)
    #print(array)
print(result)



