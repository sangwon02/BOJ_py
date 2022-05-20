n1, n2 = map(int, input().split()) #숫자 두개를 공백을 구분하여 입력 받음

print((str(n1)*n1)[:n2]) #n1을 n1번 출력한다. 
#만약 답이 길어지면 답의 앞 n2자리를 출력
