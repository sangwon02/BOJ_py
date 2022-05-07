x, y = map(int, input().split())#카드의 개수 x과 만들수 있는 최대 y
li = list(map(int, input().split())) #카드를 입력받음
num = len(li) #리스트 원소의 수

sum = 0 #카드의 합을 저장할 변수
for i in range(num): #num만큼 반복
        for j in range(i + 1, num): #i+1에서 num만큼 반복
                for k in range(j + 1, num):#j+1에서 num만큼 반복
                        if li[i] + li[j] + li[k] > y: #li[i], li[j], li[k]합이 y보다 크면 다시 위로 돌아감
                                continue
                        else: #li[i], li[j], li[k]합이 y보다 작으면 
                                sum = max(sum, li[i] + li[j] + li[k]) #sum과 합중에 큰것을 sum에 저장
#sum 출력
print(sum)