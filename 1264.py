import sys

while True:
    line = sys.stdin.readline().rstrip()
    
    if line == '#':
        break
    
    line = line.lower()
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for char in line:
        if char in vowels:
            count += 1
            
    print(count)