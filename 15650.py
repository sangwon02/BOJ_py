n, m = map(int, input().split())
li = []

def dfs(now):
  if len(li) == m: # 숫자의 개수가 m개이면
    print(' '.join(map(str, li))) # 수열을 출력
    return

  for i in range(now, n+1): # n까지 반복
    if i not in li: # 리스트안에 i가 없다면
      li.append(i) # i를 추가해줌
      dfs(i+1) # 현재 숫자보다 큰 숫자만 탐색
      li.pop()
    
dfs(1)