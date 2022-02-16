h, m = input().split()  
h = int(h)
m = int(m)

if h>=0 and h<=23 and m>=0 and m<=59:
    if m>=45:
        m = m-45
        print(h, m)
    else:
        if h==0:
            h = 23
            m = m + 15
            print(h, m)
        else:
            h = h-1
            m = m + 15
            print(h, m)