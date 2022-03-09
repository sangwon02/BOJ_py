n1, n2 = map(int, input().split())
m1, m2 = map(int, input().split())

while 1:
    n2 = n2 - m1
    m2 = m2 - n1
    if n2<=0 and m2<=0:
        print("DRAW")
        break
    elif n2 <= 0:
        print("PLAYER B")
        break
    elif m2 <= 0:
        print("PLAYER A")
        break