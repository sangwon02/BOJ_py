A = []
length = []

for i in range(5):
    r = input()
    A.append(r)
    length.append(len(r))

st = ""

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            st += A[j][i]

print(st)