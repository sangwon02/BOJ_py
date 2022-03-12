n = int(input())

for i in range(n):
    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))
    sum1 = li1[0] + li1[1]*2 + li1[2]*3 + li1[3]*3 + li1[4]*4 + li1[5]*10
    sum2 = li2[0] + li2[1]*2 + li2[2]*2 + li2[3]*2 + li2[4]*3 + li2[5]*5 + li2[6]*10
    if sum1 > sum2:
        print("Battle %d: Good triumphs over Evil"%(i+1)) 
    elif sum1 < sum2:
        print("Battle %d: Evil eradicates all trace of Good"%(i+1)) 
    else:
        print("Battle %d: No victor on this battle field"%(i+1)) 