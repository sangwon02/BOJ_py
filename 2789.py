str1 = input()
str2 = ""
str_list = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]

for i in str1:
    if i not in str_list:
        str2 += i

print(str2)