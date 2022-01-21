n = int(input())
num1 = 1

while n>num1:
    n-=num1
    num1+=1

if num1%2==0:
    a=n 
    b=num1-n+1
    
else:
    a=num1-n+1
    b=n
print(a, '/', b, sep='')