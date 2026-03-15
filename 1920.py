import sys
input = sys.stdin.readline

def binary_search(array, target):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        mid = (start + end) // 2 
        
        # 값을 찾은 경우
        if array[mid] == target:
            return 1
        # 중간값이 타겟보다 큰 경우 -> 왼쪽 탐색
        elif array[mid] > target:
            end = mid - 1
        # 중간값이 타겟보다 작은 경우 -> 오른쪽 탐색
        else:
            start = mid + 1
            
    # 반복문이 끝날 때까지 못 찾았다면 없는 것
    return 0

n = int(input())
li1 = list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))

li1.sort()

for i in li2:
    print(binary_search(li1, i))