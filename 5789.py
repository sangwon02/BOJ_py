N = int(input())

for i in range(N):
    s = input()
    if s[len(s)//2] == s[len(s)//2 -1]:  
        print("Do-it")
    else: 
        print("Do-it-Not")