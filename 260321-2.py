n = int(input())
li = []

for i in range(n-1):
    li.append(list(map(int, input().split())))

    
for a in range(1, n-1):
    for b in range(a+1, n):
        for c in range(b+1, n+1):
            
            cost_ab = li[a-1][b-a-1]
            cost_bc = li[b-1][c-b-1]
            cost_ac = li[a-1][c-a-1]
            
            if cost_ab + cost_bc < cost_ac:
                print("Yes")
                exit()
                
print("No")