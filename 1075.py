n1 = input()
n2 = int(input())

n3 = int(n1[:-2] + '00')

while(n3%n2 != 0):
    n3 += 1

print(str(n3)[-2:])
    