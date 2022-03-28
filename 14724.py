n=input()
license=['PROBRAIN','GROW','ARGOS','ADMIN','ANT','MOTION','SPG','COMON','ALMIGHTY']
limax=[]
for i in range(9):
    limax.append (max(list(map(int, input().split()))))
check=max(limax)

for i in range(9):
    if check ==limax[i]: 
        print (license[i]); 
        break