import sys

n = int(sys.stdin.readline())
company = []

for i in range(n):
    name, play = sys.stdin.readline().split()
    if play=="enter":
        company.append(name)
    else:
        company.remove(name)

company.sort(reverse=True)

for i in company:
    print(i)

#계속 시간 초과라고 뜨는데 왜 시간 초과인지 모르겠다. 나중에 한번 알아봐야겠다.