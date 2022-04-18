n1, n2 = map(int, input().split())
a, b = n1, n2 
while b != 0: 
    a = a % b 
    a, b = b, a 

print(a) 
print(n1*n2//a)