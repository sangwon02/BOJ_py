import re

n = int(input())
sum1=0
str1 = input()

li = re.findall("\d+", str1)

for i in li:
    sum1 += int(i)
print(sum1)