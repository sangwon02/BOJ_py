li = list(map(int, input().split()))
if len(li) == 1:
    print("Good")
    exit()
    
for i in range(len(li)):
    
    if li[i] > li[i+1]:
        print("Bad")
        exit()

print("Good")