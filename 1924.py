Day = 0
li1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
li2 = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
n1, n2 = map(int,input().split())
 
for i in range(n1-1):
    Day = Day + li1[i]
Day = (Day + n2) % 7
 
print(li2[Day])