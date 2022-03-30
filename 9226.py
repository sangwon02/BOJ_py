str2 =""
str1 =input()
while str1 != "#":
    str1 = input()
    for i in range(len(str1)):
        if str1[i] == 'a' or str1[i] == 'e' or str1[i] == 'i' or str1[i] == 'o' or str1[i] == 'u':
            print(str1[i:],str2,"ay")
            continue
        else:
            str2 = str2 + str1[i]