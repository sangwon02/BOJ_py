N, W, H, L= map(int, input().split())

n1 = W//L
n2 = H//L
num = n1*n2

if num>=N:
    print(N)
else:
    print(num)