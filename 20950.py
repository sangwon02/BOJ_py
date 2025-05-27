from sys import stdin
input=stdin.readline

n=int(input())
inks=[] 

for i in range(n):
    r,g,b=map(int,input().split()) 
    inks.append([r,g,b])

gomduri=list(map(int,input().split()))

ans=1000 

def bt(mixtime,nowrgb,idx): 
    global ans
    if 1<mixtime:
        dif=0
        for i in range(3):
            dif+=abs(nowrgb[i]//mixtime-gomduri[i])
        ans=min(ans,dif)
        if mixtime==7: 
            return

    for i in range(idx,n):
        newrgb=[]
        for j in range(3): 
            newrgb.append(nowrgb[j]+inks[i][j])
        bt(mixtime+1,newrgb,i+1)
        
        
for idx,ink in enumerate(inks):
    bt(1,ink,idx+1)

print(ans)