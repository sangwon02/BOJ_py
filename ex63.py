#에라토스테네스의 체란을 사용함

n1, n2 = map(int, input().split())

n2 += 1     
prime = [True] * n2  
for i in range(2, int(n2**0.5)+1): 
    if prime[i]:               
        for j in range(2*i, n2, i):   
            prime[j] = False

for i in range(n1, n2):
    if i > 1 and prime[i] == True: 
        print(i)