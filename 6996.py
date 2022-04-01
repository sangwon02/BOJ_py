N = int(input())
for i in range(N):
    s1, s2 = input().split()
    li1 = list(s1)
    li2 = list(s2)
    li1.sort(reverse=False)
    li2.sort(reverse=False)
    
    if li1 == li2:
        print(s1, "&", s2, "are anagrams.")
    else:
        print(s1, "&", s2, "are NOT anagrams.")