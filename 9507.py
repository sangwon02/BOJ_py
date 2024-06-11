import sys
input = sys.stdin.readline

koong = [1,1,2,4]  # 일단 koong(0)부터 koong(3)까지 저장

for _ in range(int(input())):
    n = int(input())
    for i in range(len(koong)-1, n):  # n이 저장해둔 값보다 크면
        koong.append(koong[i]+koong[i-1]+koong[i-2]+koong[i-3])  # 그 값 만큼 생성 후 저장
    print(koong[n])  # 답 출력