import sys
n = int(sys.stdin.readline())

li1 = []
li2 = []

for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    for j in range(1, int(n1**(1/2)) + 1):
        if (n1 % j == 0):
            li1.append(j) 
            if ( (j**2) != n1) : 
                li1.append(n1 // j)

    for j in range(1, int(n2**(1/2)) + 1):
        if (n2 % j == 0):
            li2.append(j) 
            if ( (j**2) != n2) : 
                li2.append(n2 // j)

    set1 = set(li1)
    set2 = set(li2)
    set3 = set1 | set2 
    li3 = list(set3)
    num = 1
    for j in li3:
        num = n*j

    print(num)

        

