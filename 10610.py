import sys
from itertools import permutations
input = sys.stdin.readline

n = input().strip()  # 길거리에 찾은 수 입력 받음
li = list(n)

if '0' not in n:  # 만약 0이 없다면 10의 배수가 될 수 없으니
    print(-1)  # -1 출력
else:
    num = 0
    for i in n:  # 찾은 수의 포함된 숫자를 모두 더 해주고
        num += int(i)
    if num % 3 != 0:  # 3으로 나누어지지 않는다면
        print(-1)  # 3의 배수가 되지 않으니 -1 출력
    else:  # 위에 두 조건을 모두 만족하면  
        li.sort(reverse=True)  # 내림차순으로 정렬하면
        result = int(''.join(li))  # 원하는 답이 나옴
        print(result)
        