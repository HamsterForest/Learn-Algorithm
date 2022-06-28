"""
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서
회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 
동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 
회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 
같은 자연수 또는 0이다.
"""
import sys
n=int(input())
hoe=[]#회의 시작 끝시각,#회의시간

for i in range(n):
    hoe.append(list(map(int,sys.stdin.readline().split())))
    hoe[i].append(hoe[i][1]-hoe[i][0])


hoe.sort(key=lambda x:(x[0],x[2])) #회의시작시간을 기준으로 오름차순 정렬하고 같다면, 회의시간으로 오름차순정렬
#print(hoe)

count=0#회의 수
pre=[[0,0,0]]#이전회의의 종료시간

for i in hoe:
    #print(pre)
    if i==[0,0,0]:
        count+=1
        break
    #if i==pre[0]:
    #    continue#중복회의제거
    if i[0]>pre[0][0] and i[1]<pre[0][1]:#이번의 순서가 전 회의시간 안에 포함되는 경우 이로 대체
        pre[0]=i
        continue
    if i[0]>=pre[0][1]:
        #print("진입")
        #print(i)
        #print("탈출")
        count+=1
        pre[0]=i

print(count)
