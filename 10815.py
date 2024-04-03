n = int(input())
n_num = list(map(int, input().split()))  # 상근이가 가지고 있는 카드

m = int(input())
m_num = list(map(int, input().split()))  # 비교할 카드

n_num_dict = {}  # 속도는 dictionary가 빠름
for i in n_num:
    n_num_dict[i] = 0

for i in m_num:  # 비교할 카드를 하나하나 꺼내고
    if i in n_num_dict:  # 만약 상근이 손에 있다면
        print("1",end=" ")  # 1 출력
    else:  # 없다면
        print("0",end=" ")  # 0 출력