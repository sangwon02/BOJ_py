str1 = input()
str_list = list(str1)
check = "true"

for i in range(len(str1)//2 + 1):
    if str_list[i] != str_list[-(i+1)]:
        check = "false"

print(check)