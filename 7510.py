n = int(input())

for i in range(n):
    li = list(map(int, input().split()))
    li.sort(reverse=False)
    if li[2]**2 == li[1]**2 + li[0]**2:
        print("Scenario #%d:"%(i+1))
        print("yes")
        print("")
    else:
        print("Scenario #%d:"%(i+1))
        print("no")
        print("")
    
