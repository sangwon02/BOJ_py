#한수는 지금 (x, y)에 있다. 
#직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
#직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
x, y, w, h = map(int, input().split())

n1 = w-x
n2 = h-y
n3 = x
n4 = y
#print(min(n1, n2, n3, n4)) 쓰면 끝남

if n1 <= n2:
    if n1 <= n3:
        if n1 <= n4:
            print(n1)
        else:
            print(n4)
    else:
        if n3 <= n4:
            print(n3)
        else:
            print(n4)
else:
    if n2 <= n3:
        if n2 <= n4:
            print(n2)
        else:
            print(n4)
    else:
        if n3 <= n4:
            print(n3)
        else:
            print(n4)

