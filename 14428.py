import sys
import math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())

block_size = int(math.sqrt(N)) + 1 # 블럭의 크기를 루트 N으로 설정
num_blocks = math.ceil(N / block_size) # 올림을 통해 블럭의 개수 구함

# 각 블록의 최솟값 인덱스 저장할 리스트
block_min_idx = [-1] * num_blocks

# 두 인덱스 중 값이 더 작거나, 값이 같다면 인덱스가 작은 것을 고르는 함수
def get_min_idx(idx1, idx2):
    if idx1 == -1: return idx2
    if idx2 == -1: return idx1
    if A[idx1] <= A[idx2]: return idx1
    return idx2

# 초기 블록 세팅
for i in range(N):
    b = i // block_size # 현재 자리가 속한 블록
    block_min_idx[b] = get_min_idx(block_min_idx[b], i)

result = []

for _ in range(M):
    query_data = list(map(int, input().split()))
    
    if query_data[0] == 1:
        # 1번 쿼리 (업데이트)
        i, v = query_data[1] - 1, query_data[2] # 0-based 인덱스로 변환
        A[i] = v
        
        # 값이 바뀌었으니 해당 블록의 최솟값 인덱스만 다시 계산
        b = i // block_size
        block_min_idx[b] = -1 # 초기화 후
        for j in range(b * block_size, min((b + 1) * block_size, N)):
            block_min_idx[b] = get_min_idx(block_min_idx[b], j)
            
    else:
        # 2번 쿼리 (구간 최솟값 인덱스 조회)
        a, b = query_data[1] - 1, query_data[2] - 1
        answer_idx = -1
        
        start_block = a // block_size
        end_block = b // block_size    
        
        if start_block == end_block:
            for i in range(a, b + 1): 
                answer_idx = get_min_idx(answer_idx, i)
        else:
            # 왼쪽 블록(첫번째)에서 탐색
            for i in range(a, (start_block + 1) * block_size):
                answer_idx = get_min_idx(answer_idx, i)
            # 중간 블록들 탐색 (미리 구해둔 최솟값 인덱스 사용)
            for i in range(start_block + 1, end_block):
                answer_idx = get_min_idx(answer_idx, block_min_idx[i])
            # 오른쪽 블록(마지막)에서 탐색
            for i in range(end_block * block_size, b + 1):
                answer_idx = get_min_idx(answer_idx, i)
                
        # 1부터 시작하는 인덱스이기에 +1
        result.append(str(answer_idx + 1))

print('\n'.join(result))