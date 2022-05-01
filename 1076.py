name = ["black" , "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
multi = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
#색에 따른 저항값을 저장해준다.
s1 = input()  
s2 = input()  
s3 = input()  

n1 = name.index(s1)*10 #첫번째 입력 받은 것의 인덱스의 값에 10을 곱해준뒤 n1에 저장
n2 = name.index(s2) #두번째 입력 받은 것의 인덱스의 값을 n2에 저장
n3 = multi[name.index(s3)] #세번째 입력 받은 것의 곱을 n3에 저장

print((n1+n2)*n3) #저항값을 계산해준다.