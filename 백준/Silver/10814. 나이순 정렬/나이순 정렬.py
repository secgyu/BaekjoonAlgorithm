import sys
input = sys.stdin.readline

count = int(input())
arr = []

for i in range(count):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name))

arr.sort(key = lambda x : x[0])

for i in arr:
    print(i[0], i[1])