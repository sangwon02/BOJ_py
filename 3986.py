n=int(input())
result=0

for i in range(n):
  s=input().strip()
  li=[]

  for i in s:
    if not li or li[-1]!=i:
      li.append(i)
    else:
      li.pop()
  
  if not li:
    result+=1

print(result)