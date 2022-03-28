str1 = input()
cnt1 = 0
cnt2 = 0
for i in range(len(str1)-2):
    if str1[i:i+3] == "JOI":
        cnt1 += 1
    elif str1[i:i+3] == "IOI":
        cnt2 += 1
print(cnt1)
print(cnt2)