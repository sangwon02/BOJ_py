n = int(input())

for i in range(n):
    n1, n2 = map(int, input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)."%(n1//n2,n1%n2))