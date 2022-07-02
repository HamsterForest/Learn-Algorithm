"""
가장 작은 데이터를 찾아내어 앞으로 보내는 과정을 반복하여 하는 정렬
시간 복잡도 O(N^2)
"""
#아래 리스트를 오름차순 정렬하자
array=[9,8,7,6,5,4,3,2,1,0]

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]#스와프

print(array)