a, b, c, d, e, f = map(int, input().split())

print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))  
# x의 값은 (c*e-b*f)//(a*e-b*d)를 하면 나오고
# y의 값은 (a*f-d*c)//(a*e-b*d)를 하면 나온다.

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
            print(x,y)