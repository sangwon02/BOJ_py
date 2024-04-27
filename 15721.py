import sys
input = sys.stdin.readline

a = int(input())
t = int(input())
n = int(input())
peoplecnt = 0  # 외치고 있는 사람 확인하는 변수
funcnt = 0  # 외쳐야하는 뻔,데기 확인하는 변수 
count = 0  # 구하고자 하는 구호 외쳐진 횟수
fun = [0,1,0,1,0,0,1,1]  # 현재 불러야하는 번데기 상황
while True:
    if funcnt == len(fun):  # 번데기가 한바퀴 돌았으면
        fun.insert(4, 0)  # 뻔, 데기 추가해줌
        fun.insert(-1, 1)
        funcnt = 0  # 외쳐야하는 뻔,데기 확인하는 변수 0으로 초기화
    if fun[funcnt] == n:  # 구하고자 하는 구호가 불렸으면
        count += 1  # 카운트 해줌
    if peoplecnt == a:  # 만약 사람이 한바퀴 돌았으면
        peoplecnt = 0  # 0번 사람부터 다시 시작
    funcnt += 1  # 다음 불러야하는 구호로 이동
    if t == count:  # 구하고자 하는 구호가 t만큼 불렸으면 종료
        break
    peoplecnt += 1  # 다음 사람으로 이동
    
print(peoplecnt)  # 누가 외쳤는지 출력