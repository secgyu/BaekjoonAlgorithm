import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))

for i in arr:
    print(i)
