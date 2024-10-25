import sys
input = sys.stdin.readline

li = list(input().rstrip("\n"))
result = []

for i in range(1, len(li) - 1):
    for j in range(i + 1, len(li) ):
        a = li[:i]
        b = li[i:j]
        c = li[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        result.append("".join(a + b + c))
        
result.sort(reverse=False)

print(result[0])