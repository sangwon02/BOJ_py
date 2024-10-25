nums = set(range(1, 10000))
remove_set = set()  
for num in nums :
    for n in str(num):
        num += int(n)
    remove_set.add(num)  # 생성자가 있는 수는 remove_set에 넣어서 저장

self_nums = nums - remove_set  # 차집합을 구함
for self_num in sorted(self_nums):  # 정렬 후 출력
    print(self_num)