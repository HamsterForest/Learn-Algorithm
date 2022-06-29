"""
백준 1541
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 
가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 
5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
입력으로 주어지는 식의 길이는 50보다 작거나 같다.
"""

#-가 나오면 다음 -가 나올때 까지 그 수를 괄호로 묶는다.

a=input()
num=[]
numbers=[]#실제수들
state=False
minus=False
a_length=len(a)
for i in range(a_length):
    if a[i]=='+':
        state=True
    elif a[i]=='-':
        state=True
        minus=True
    else:
        num.append(int(a[i]))
    if state==True or i==(a_length-1):#숫자를 저장
        length=len(num)
        number=0
        for j in range(length):
            number+=num[j]*(10**(length-1))
            length-=1
        numbers.append(number)
        if minus==True:
            numbers.append(0)
        minus=False
        state=False
        num=[]

pre_result=[]
length=len(numbers)
tem=0
for idx,data in enumerate(numbers):
    if data!=0:
        tem+=data
    else:
        pre_result.append(tem)
        tem=0
    if idx==(length-1):
        pre_result.append(tem)

result=pre_result[0]
for i in range(1,len(pre_result)):   
    result-=pre_result[i]

print(result)