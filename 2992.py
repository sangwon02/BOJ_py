x = input()

for i in range(6):
    if int(x[0]) < int(x[i]):
        a = x[0]
        x[0] = x[i]
        x[i] = x[0]