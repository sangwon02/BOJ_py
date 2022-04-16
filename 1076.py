name = ["black" , "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
multi = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

s1 = input()  
s2 = input()  
s3 = input()  

n1 = name.index(s1)*10
n2 = name.index(s2)
n3 = multi[name.index(s3)]

print((n1+n2)*n3)