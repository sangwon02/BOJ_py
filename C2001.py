min_pa = float('inf')
min_ju = float('inf')

for i in range(3):
    pasta = int(input())
    if min_pa > pasta:
        min_pa = pasta
        
for i in range(2):
    juice = int(input())
    if min_ju > juice:
        min_ju = juice
        
print(round((min_pa+min_ju)*1.1,1))
