st = input().upper()
num = 0
for i in st:
    if i == 'B'or i == 'C'or i == 'A':
        num +=3
    elif i == 'E'or i == 'F'or i == 'D':
        num +=4
    elif i == 'H'or i == 'I'or i == 'G':
        num +=5
    elif i == 'K'or i == 'J'or i == 'L':
        num +=6
    elif i == 'N'or i == 'O'or i == 'M':
        num +=7
    elif i == 'Q'or i == 'S'or i == 'R'or i == 'P':
        num +=8
    elif i == 'U'or i == 'V'or i == 'T':
        num +=9
    elif i == 'X'or i == 'Y'or i == 'W'or i == 'Z':
        num +=10
    else:
        num +=11
print(num)
