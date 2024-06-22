import sys
input = sys.stdin.readline

n, point, p = map(int, input().split())
if n == 0:
    print(1)
else:
    li = list(map(int, input().split()))
    if n == p and li[-1] >= point:  # 만약 랭킹 리스트에서 벗어나면
        print(-1)  # -1 출력
    else:
        rank = n + 1  # 일단은 순위를 n+1로 두고
        for i in range(n):  # 가장 높은 점수부터 탐색
            if li[i] <= point:  # 만약 태수가 달성한 점수보다 낮거나 같다면
                rank = i + 1  # 순위를 갱신해줌
                break  # for문 종료
        print(rank)  # 순위 출력