import sys
input = sys.stdin.readline

n = int(input())  # 생성자를 찾기 위한 n 입력 받고

for i in range(1, n+1):  # 가장 낮은 수부터 차례대로 생성자를 찾는다.
    sum = i  # 분해합을 담을 변수
    num = i
    while i%10: # 각 자리수를 구할 수 없을때 까지
        sum += i%10 # 각 자리수를 더해준다.
        i = i//10  
    if sum == n: # 만약 n과 같다면
        print(num)  # 답을 출력하고
        exit()  # 프로그램 종료

print(0)  # 답이 없으면 0을 출력