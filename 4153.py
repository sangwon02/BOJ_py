#직각 삼각형인지 아닌지 구별하는 문제
#피타고라스 정리 사용함

while 1:
    n1, n2, n3 = map(int, input().split())
    if n1==0 and n2==0 and n3==0:
        exit()
    elif n1**2 + n2**2 == n3**2:
        print("right")
    elif n1**2 + n3**2 == n2**2:
        print("right")
    elif n3**2 + n2**2 == n1**2:
        print("right")
    else:
        print("wrong")