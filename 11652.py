n = int(input())
num_dic = {}

for i in range(n):
    num = int(input())
    if num in num_dic:
        num_dic[num] += 1
    else:
        num_dic[num] = 1

num_dic = sorted(num_dic.items(), key=lambda x: (-x[1], x[0])) #딕셔너리 키값에 대해 내림차순으로 정렬한다
print(num_dic[0][0])