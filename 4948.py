while 1:
    n1 = int(input())
    if n1==0:
        break
    n2 = n1*2 + 1
    prime = [True] * n2  
    for i in range(2, int(n2**0.5)+1): 
        if prime[i]:               
            for j in range(2*i, n2, i):   
                prime[j] = False
    num = 0
    for i in range(n1+1, n2):
        if i >= 1 and prime[i] == True: 
            num += 1
    print(num)