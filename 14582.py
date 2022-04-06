attack_list = list(map(int, input().split()))
defense_list = list(map(int, input().split()))

result = [0]

attack_num = 0
defense_num = 0

prin = ""

for i in range(9):
    attack_num += attack_list[i]
    defense_num += defense_list[i]

    result.append(defense_num - attack_num)

    if result 