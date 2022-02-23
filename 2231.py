num = int(input()) 

for i in range(1, num+1):  
    num1 = sum((map(int, str(i)))) 
    su = i + num1

    if su == num:
        print(i)
        break
    if i == num:
        print(0) 
    
    
        
    
    