import sys
input = sys.stdin.readline

k = int(input())

for i in range(k):  # K번 반복
    li = []  # 학생 수와 점수를 받을 리스트 생성
    li = list(map(int, input().split()))  # 정보를 리스트에 받고
    num_student = li[0]  # 첫번째 수는 학생 수 이기에 num_student 저장
    del li[0]  # 학생 수는 리스트에서 빼주어 점수만 남도록 함
    li.sort(reverse=False)  # 점수를 오름차순으로 정렬
    gap = li[1] - li[0]  # 뒤에서 1,2등의 점수 차를 gap에 저장
    for j in range(num_student-2):  #이미 한번은 저장했으니까 (학생수 -2)개의 점수차이만 구하면 됨
        if (li[j+2] - li[j+1]) > gap:  # 만약 변수에 저장된 것보다 크면
            gap = li[j+2] - li[j+1]  # 새로 갱신해줌
    print("Class {}".format(i+1))  # 몇반인지 출력
    # 원하는 결과 출력
    print("Max {}, Min {}, Largest gap {}".format(li[num_student-1], li[0], gap))