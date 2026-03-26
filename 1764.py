n, m = map(int, input().split())

n_set = set()
m_set = set()


for _ in range(n):
    st = input()
    n_set.add(st)
    
for _ in range(m):
    st = input()
    m_set.add(st)
    
print(len(n_set&m_set))

res = list(n_set&m_set)

res.sort()

for i in res:
    print(i)