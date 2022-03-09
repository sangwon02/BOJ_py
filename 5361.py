n = int(input())
li = []

for i in range(n):
    n1, n2, n3, n4, n5 = map(int, input().split())
    li.append(n1*350.34+n2*230.90+n3*190.55+n4*125.30+n5*180.90) 

for j in li:
    print("${:.2f}".format(j))

