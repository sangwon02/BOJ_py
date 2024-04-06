from itertools import combinations, permutations
import sys
n, m = map(int, sys.stdin.readline().split())

nums = []
for i in range(n):
    nums.append(i+1)

perm = list(permutations(nums, m))

for i in perm:
    print(" ".join(map(str, i)))
#####################################################
import sys
input = sys.stdin.readline

def backtracking():
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    for i in range(1, n+1):
        if i not in array:
            print(array, "1")
            array.append(i)
            print(array, "2")
            backtracking()
            print(array, "3")
            array.pop()
            print(array, "4")

n, m = map(int,input().split())
array = []

backtracking()