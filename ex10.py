x, y, z= input().split()  
x = int(x)
y = int(y)
z = int(z)

print((x+y)%z)
print(((x%z)+(y%z))%z)
print((x*y)%z)
print(((x%z)*(y%z))%z)

