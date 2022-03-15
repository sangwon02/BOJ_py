str1 = input()
cnt = 0
for i in str1:
    print(i, end ="")
    cnt += 1
    if cnt%10==0:
        print(" ")
