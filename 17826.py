li = list(map(int, input().split()))
n = int(input())

rank = li.index(n, 0, 50) + 1

if rank >= 1 and rank <= 5:
    print("A+")
elif rank >= 6 and rank <= 15:
    print("A0")
elif rank >= 15 and rank <= 30:
    print("B+")
elif rank >= 31 and rank <= 35:
    print("B0")
elif rank >= 36 and rank <= 45:
    print("C+")
elif rank >= 46 and rank <= 48:
    print("C0")
else:
    print("F")
