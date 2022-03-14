n = int(input())

for i in range(n):
    str = input()
    li = list(str)
    sum = 0
    for j in li:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")
