def fun(n): #피보나치 수 리턴 함수
    if n <= 1: #n이 1보다 작거나 같으면 
        return n #리턴 n

    return fun(n-1) + fun(n-2) #Fn = Fn-1 + Fn-2 (n ≥ 2) 피보나치 수 리턴

n = int(input()) #숫자 입력 받음

print(fun(n)) #피보나치 수 프린트