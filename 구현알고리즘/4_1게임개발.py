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
#맵의 크기 입력
n,m=map(int,input().split())
#캐릭터의 좌표와 바라보는 방향 0:북 1:동 2:남 3:서
x,y,c_dir=map(int,input().split())
#맵의 작성
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

dir_list=[3,2,1,0]#계속 왼쪽으로 이동하기 위함
dir_idx=0
for idx, data in enumerate(dir_list):#현재 바라보고 있는 방향
    if c_dir==data:
        dir_idx=idx

goto_list=[(-1,0),(0,1),(1,0),(0,-1)]#방향별 이동 좌표 서남동북

def turnleft(dir_idx):#회전하는 인덱스 dir_list를 위함
    if dir_idx<3:
        dir_idx+=1
    elif dir_idx==3:
        dir_idx=0
    return dir_idx

count_turn=0
blocked=False#만약 사방이 갈 수 없는 상화이라면
result_count=0#총 몇 번 이동?

for i in range(100):
    array[x][y]=2
    print(array)
    print(x,y,c_dir)
    #반시계방향으로 한번 회전
    dir_idx=turnleft(dir_idx)
    c_dir=dir_list[dir_idx]
    #회전횟수를 카운트
    count_turn+=1

    if count_turn==4:
        blocked=True
        count_turn=0
    #회전한 방향쪽이 바다가 아니고 이미 가본곳이 아니면 그 방향으로 이동

    if blocked==False:
        if array[x+goto_list[c_dir][0]][y+goto_list[c_dir][1]]!=2 and array[x+goto_list[c_dir][0]][y+goto_list[c_dir][1]]!=1:
            x+=goto_list[c_dir][0]
            y+=goto_list[c_dir][1]
            result_count+=1
            count_turn=0
    else:#가던 방향의 반대 방향으로 한 칸 이동
        #그 곳에 바다가 있지 않으면 뒤로 이동
        if array[x+goto_list[c_dir][0]*-1][y+goto_list[c_dir][1]*-1]!=1:
            x+=goto_list[c_dir][0]*-1
            y+=goto_list[c_dir][1]*-1
            result_count+=1
            blocked=False

        else:
            break

   
print(result_count)