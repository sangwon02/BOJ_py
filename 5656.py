cnt=1
while True:
    n1,s,n2=input().strip().split()
    if s=="E":
        break
    if s=="!=":
        print("Case {}: ".format(cnt)+str(int(n1)!=int(n2)).lower())
    elif s=="<":
        print("Case {}: ".format(cnt)+str(int(n1)<int(n2)).lower())
    elif s=="<=":
        print("Case {}: ".format(cnt)+str(int(n1)<=int(n2)).lower())
    elif s==">":
        print("Case {}: ".format(cnt)+str(int(n1)>int(n2)).lower())
    elif s==">=":
        print("Case {}: ".format(cnt)+str(int(n1)>=int(n2)).lower())
    elif s=="==":
        print("Case {}: ".format(cnt)+str(int(n1)==int(n2)).lower())
    cnt+=1