vowel = ['a','e','i','o','u']
while 1:
    s = input()
    if s=='#' : 
        break
    li = []
    for i in s: 
        li.append(i)

    if 'a' not in li and 'e' not in li and 'i' not in li and 'o' not in li and 'u' not in li:
        print(s+"ay")
    
    else:
        while li[0] not in vowel :
            li.append(li[0])
            del li[0]
        for i in li:
            print(i,end='')
        print("ay")