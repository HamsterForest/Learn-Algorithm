#리스트 원소의 수와 찾고자하는 값
n,target=list(map(int,input().split()))
#리스트 전체
array=list(map(int,input().split()))

def binary_search(array, target, start, end):
    while start<=end:
        #중간지점 지정
        mid=(start+end)//2
        #중간지점이 찾고자하는 것이 맞으면
        if array[mid]==target:
            return mid
        #목표값이 중간지점보다 작을 경우 끝지점을 중간지점 전 인덱스로
        elif array[mid]>target:
            end=mid-1
        #목표값이 중간지점보다 클 경우 끝지점을 중간지점보다 큰 인덱스로
        else:
            start=mid+1
    return None

result=binary_search(array,target,0,n-1)

if result==None:
    print("해당 원소가 존재하지 않습니다.")
else:
    print(result+1)