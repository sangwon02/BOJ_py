import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li = []

for i in range(n):  # n번 만큼 나라와 메달 입력 받음
    name, gold, silver, bronze = map(int,input().split())
    li.append([name, gold, silver, bronze])

# 받은 메달들 정렬
li.sort()

namek, kg, ks, kb = li[k-1]
rank = 1

# 메달 리스트 순환하며 K나라와 비교
for name, g, s, b in li :
  if  name == namek :  # 만약 찾는 이름과 같은 나라를 찾을때는
    continue  # 등수 +1 하지 않고 다음 나라와 비교 
  
  # 만약 K나라보다 성적이 좋다면 
  if g > kg or g == kg and s > ks or g == kg and s == ks and b > kb : 
    rank += 1  # K나라의 등수 +1

print(rank)  # K나라의 등수 출력
