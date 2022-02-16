n = int(input())
cnt = 0
for i in range(n):
    str = input()
    no = 0
    for j in range(len(str)-1):
        if str[j] != str[j+1]:
            new_str = str[j+1:]
            if new_str.count(str[j]) >=1:
                
                no += 1
    if no == 0:
        cnt += 1
print(cnt) 