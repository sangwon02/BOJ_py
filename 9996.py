n = int(input())
s1, s2 = input().split("*")
len1 = int(len(s1))
len2 = int(-len(s2))
for i in range(n): 
    s = str(input())
    if len(s)<len(s1)+len(s2):
        print("NE")
    elif s1 == s[:len1] and s2 == s[len2:]:
        print("DA")
    else:
        print("NE")
