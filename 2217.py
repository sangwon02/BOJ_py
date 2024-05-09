import sys
input = sys.stdin.readline

n = int(input()) 
li = []
for i in range(n):  # 로프들의 개수만큼
    s = int(input())  # 로프가 버티는 무게를 토대로
    li.append(s)  # 리스트에 저장
    
li.sort(reverse=True)  # 내림차순으로 정리해주고
final = li[i]  # 가장 큰 무게를 버티는 로프를 일단 최종 값에 저장

for i in range(n):
    if final < li[i]*(i+1):  # 만약 최종값보다 버티는 로프의 무게가 크다면
        final = li[i]*(i+1)  # 그 값으로 바꾸어줌
        
print(final)  # 최종값 출력