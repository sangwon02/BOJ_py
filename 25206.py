li1 = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
li2 = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0	
result = 0	

for _ in range(20) :
    name, credit, lank = input().split()
    credit = float(credit)

    if lank != 'P' :
        total += credit
        result += credit * li2[li1.index(lank)]

print(round((result / total), 6))