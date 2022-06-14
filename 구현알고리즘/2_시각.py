"""
1. 정수 n이 주어짐
2. 00시 00분 00초 ~ n시 59분 59초 의 시간중 3이 하나라도 포함되는 경우의 수를 센다.
"""
n=int(input())
count=0

for i in range(n+1):
    for j in range(60):        
        for k in range(60):
            if "3" in str(k) or "3" in str(j) or "3" in str(i):
                count+=1

print(count)
