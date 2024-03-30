a, b, c, d, e, f = map(int, input().split())

print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))  
# x의 값은 (c*e-b*f)//(a*e-b*d)를 하면 나오고
# y의 값은 (a*f-d*c)//(a*e-b*d)를 하면 나온다.