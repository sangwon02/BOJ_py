import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())

nummap = [[0]*(c + 1)]
summap = []
for _ in range(r):  # 사진의 밝기 입력 받음
    nums = [0] + [int(x) for x in input().split()]
    nummap.append(nums)
    
for i in nummap:  # summap으로 변환
    sum = 0
    nums = []
    for j in i:
        sum += j
        nums.append(sum)
    summap.append(nums)

    
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())  # 일부분의 좌표 입력 받음
    result  = 0  # 일부분의 총 밝기를 저장 할 변수
    cnt = (r2-r1+1)*(c2-c1+1)  # 일부분의 타일의 개수
    for i in range(r1, r2+1):  # 일부분의 밝기들을 저장해주고
        result += summap[i][c2] - summap[i][c1-1]
        
    print(result//cnt)  # 나누어 주어서 출력