import sys

while True:
    str1 = sys.stdin.readline().rstrip('\n')

    if not str1:
        break

    n1, n2, n3, n4 = 0, 0, 0, 0
    for each in str1:
        if each.islower():
            n1 += 1
        elif each.isupper():
            n2 += 1
        elif each.isdigit():
            n3 += 1
        elif each.isspace():
            n4 += 1
    print(n1, n2, n3, n4)