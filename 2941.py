cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
st = input()

for i in cro:
    st = st.replace(i, '*')  
    
print(len(st))