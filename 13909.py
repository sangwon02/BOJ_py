n = int(input())
window = []
for i in range(n+1):
    window.append(0)

for i in range(n):
    cnt = 1
    j = i + 1

    while j*cnt <= n:
        if window[j*cnt] == 0:
            window[j*cnt] = 1
        else:
            window[j*cnt] = 0
        cnt += 1

print(window.count(1))

n = int(input())
print(int(n**(1/2)))