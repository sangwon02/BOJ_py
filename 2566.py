A = []
m = 0
mr = 1
mc = 1
for i in range(9):
    r = list(map(int, input().split()))
    A.append(r)

for row in range(9):
    for col in range(9):
        if A[row][col]>m:
            m = A[row][col]
            mr = row+1
            mc = col+1
    
print(m)
print(mr, mc)
    