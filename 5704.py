while True:
    cnt = [0] * 26
    try :
        s = input()
        if s == "*": 
            exit()
        else:
            for i in range(len(s)):
                if ord(s[i])!=32 :
                    cnt[ord(s[i]) - 97]=1
            if sum(cnt) == 26: 
                print("Y")
            else: 
                print("N")

    except : exit()