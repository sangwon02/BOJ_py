n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    cnt = 0
    for j in range(len(str1)):
        if str1[j] != str2[j]:
            cnt += 1
    print("Hamming distance is %d."%cnt)