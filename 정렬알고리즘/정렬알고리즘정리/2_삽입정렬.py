"""
시간복잡도
O(N^2) for문이 이중
최선의 경우 O(N)
"""
array=[9,8,7,6,5,4,3,2,1,0]
for i in range(1,len(array)):#index 1은 이미 정렬되어 있다 가정하고 그 다음 부터 검사
    for j in range(i,0,-1):#i 부터 0까지 1식 감소 하는 for문
        if array[j]<array[j-1]:#왼쪽의 수가 지금 수보다 큰경우 왼쪽과 자기자신을 스와프한다.
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break

print(array)