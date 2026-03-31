import sys
input = sys.stdin.readline

n = int(input())
n_st = input().strip()
m = int(input())
m_st = input().strip()

if set(m_st) - set(n_st):  # 만들 수 없는 문자면 -1 출력
    print(-1)
else:
    index = n-1 
    rotations = 0
    
    for i in m_st: # 만들어야하는 문자로 돌림
        while True:
            index = (index+1) % n # 다음 돌림판 탐색
            rotations += 1
            if n_st[index] == i: # 문자 탐색했으면
                break
                
    print(rotations)