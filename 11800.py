n = int(input())

for i in range(n):
    n1, n2 = map(int, input().split())
    if n2 < n1:
        s = n1
        n1 = n2
        n2 = s
    print("Case %d:"%(i+1), end=" ")
    if n1 == 1:
        if n2 == 1:
            print("Habb Yakk")
        elif n2 == 2:
            print("Doh Yakk")
        elif n2 == 3:
            print("Seh Yakk")
        elif n2 == 4:
            print("Ghar Yakk")
        elif n2 == 5:
            print("Bang Yakk")
        else:
            print("Sheesh Yakk")
    elif n1 == 2:
        if n2 == 2:
            print("Dobara")
        elif n2 == 3:
            print("Seh Doh")
        elif n2 == 4:
            print("Ghar Doh")
        elif n2 == 5:
            print("Bang Doh")
        else:
            print("Sheesh Doh")
    elif n1 == 3:
        if n2 == 3:
            print("Dousa")
        elif n2 == 4:
            print("Ghar Seh")
        elif n2 ==5:
            print("Bang Seh")
        else:
            print("Sheesh Seh")
    elif n1 == 4:
        if n2 == 4:
            print("Dorgy")
        elif n2 == 5:
            print("Bang Ghar")
        else:
            print("Sheesh Ghar")
    elif n1 == 5:
        if n2 == 5:
            print("Dabash")
        else:
            print("Sheesh Beesh")
    else:
        print("Dosh")