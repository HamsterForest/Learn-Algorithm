"""
퀵정렬의 기본적인 개요 : 기준데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를
바꾸는 것.

기준데이터: '피벗'이라고 부름
피벗은 리스트에서 첫 번째 데이터를 사용함.

1. 리스트에서 첫 번째 데이터를 피벗으로 정한다.
2. 피벗을 설장한 뒤, 왼쪽에서부터 피벗보다 큰 데이터를, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
3. 큰 데이터와 작은 데이터를 스왑한다.
4.2~3을 반복하는데 왼쪽이나 오른쪽에서 진행하다 더이상 피벗보다 큰 데이터타 작은 데이터가 없을 경우 
찾는 값의 위치가 서로 엇갈리게 된다. 이때 반복을 멈춘다.
5. 4번 단계에서 지정된 두 숫자 중 작은수와 피벗을 스왑한다.
-이제 피벗 이전의 모든 수는 피벗보다 작은 수이고 이후 수는 피벗보다 큰 수 이다.
6. 피벗을 중심으로 분할된 두 리스트에 각각 1~5를 반복한다.
-새로운 피벗은 재귀함수를 통해 깊은 함수로 들어갈때 자동으로 리스트의 첫 번째 원소로 결정된다.

퀵정렬의 시간복잡도
->평균적으로 O(NlogN)
-> 최악의 경우 O(N^2)->리스트의 첫 번째 원소를 피벗으로 삼는 경우 이미 데이터가 정렬되어 있는 경우가
최악의 경우다.
"""

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end:#원소가 1개인 경우 종료
        return
    
    pivot=start#피봇은 리스트의 첫 번째 원소
    left=start+1
    right=end
    print("\n피봇: {0} left: {1} right: {2}".format(pivot,left,right))
    while left<=right:#대 while문-엇갈림이 발생하면 깨짐
        while left<=end and array[left]<=array[pivot]:#왼쪽부터 탐색하는 부분, 피벗보다 큰 데이터를 찾을 때까지 이동
            left+=1
        print(left)
        while right > start and array[right]>=array[pivot]:#오른쪽부터 탐색하는 부분, 피벗보다 작은 데이터를 찾을 때까지 이동
            right-=1
        print(right)
        if left>right:#만약 4번과정처럼 엇갈림이 발생할경우 오른쪽에서 오던 부분고 피벗을 스왑,이 과정이후 대 while문 종료
            array[right],array[pivot]=array[pivot],array[right]
        else:#3번과정 피벗보다 큰 수와 작은수를 스왑한다.
            array[left],array[right]=array[right],array[left]
        print(array)

    quick_sort(array,start,right-1)#피벗 왼쪽 리스트를 재귀적으로 정렬
    quick_sort(array,right+1,end)#피벗 오른쪽 리스트를 재귀적으로 정렬

print("초기 상태는")
print(array)
print("정렬과정은")
quick_sort(array,0,len(array)-1)
print("따라서")
print(array)
