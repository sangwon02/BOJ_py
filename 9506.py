n = 0

while True:
    n = int(input()) 
    if n == -1:
        break
    total = 0 

    for a in range(1, n): 
        if n % a == 0:
            total += a  
    if total == n:
        print("{} = 1".format(n), end = " ")
        for a in range(2, n): 
            if n % a == 0:
                print("+ {}".format(a), end = " ")
        print(" ")

    else:
        print("{} is NOT perfect.".format(n))

        