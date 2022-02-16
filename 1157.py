st = input().upper()
st1 = list(set(st))

li = []
for x in st1 :
    cnt = st.count(x)
    li.append(cnt) 

if li.count(max(li)) > 1 :  
    print('?')
else :
    max_index = li.index(max(li)) 
    print(st1[max_index])