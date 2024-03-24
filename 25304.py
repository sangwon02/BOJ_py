x = int(input())
n = int(input())

sum = 0
for i in range(n):
  x1, x2 = map(int, input().split())
  sum += (x1*x2)

if x == sum:
  print("Yes")
else:
  print("No")