n = int(input())
str1 = input()
str_list = list(str1)

for i in range(n):
    if str_list[i] == "?" and str_list[-(i+1)] == "?":
        str_list[i] = "a"
        str_list[-(i+1)] = "a"
    elif str_list[i] == "?":
        str_list[i] =str_list[-(i+1)]

print("".join(str_list))