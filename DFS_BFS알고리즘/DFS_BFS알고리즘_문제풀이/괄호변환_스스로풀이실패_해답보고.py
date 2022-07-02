"""
컨셉 : 다른 개발자가 작성한 소스코드를 분석하여 문제점을 발견하고 수정하라는 업무과제를 받음
1. 소스코드내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 상태로 작성됨을 발견함
2. 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 개발

"""
def balance(p):#(의 수와 )의 수가 같은순반에 인덱스 반환
    count=0
    for i in range(len(p)):
        if p[i]=="(":
            count+=1
        if p[i]==")":
            count-=1
        if count==0:
            return i

def right(p):
    if p[0]==")":
        return False
    else:
        return True
            

def solution(p):
    answer=""
    if p == "":
        return answer
    index=balance(p)
    u=p[:index+1]
    v=p[index+1:]
    if right(u):
        answer=u+solution(v)
    else:
        answer="("
        answer+=solution(v)
        answer+=")"
        u=u[1:]
        u=u[:1]
        print(u)
        list(u)
        print(u)
        for i in range(len(u)):
            if u[i]=="(":
                u[i]=")"
            else:
                u[i]="("
        answer+="".join(u)
    return answer
    
string="))(("
print(solution(string))


