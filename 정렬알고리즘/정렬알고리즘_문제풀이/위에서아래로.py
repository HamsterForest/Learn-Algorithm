"""
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를
큰 수 부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

첫째 줄 수열에 속해있는 수의 개수 N이 주어진다.(1<=N<=500)
둘때 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1~100000이하의 자연수
"""

import sys

n=int(input())
array=[]
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort(reverse=True)

for i in range(n):
    print(array[i],end=' ')
