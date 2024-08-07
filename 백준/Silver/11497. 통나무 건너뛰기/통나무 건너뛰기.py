def min_difficult(woods):
    woods.sort()
    left = []
    right = []

    for i in range(len(woods)):
        if i % 2 == 0:
            left.append(woods[i])
        else:
            right.append(woods[i])
    
    arrange = left + right[::-1]

    max_difficult = 0

    for i in range(len(arrange)):
        max_difficult = max(max_difficult, abs(arrange[i] - arrange[i-1]))
   
    return max_difficult


T = int(input())
result = []

for _ in range(T):
    N = int(input())
    woods = list(map(int, input().split()))
    result.append(min_difficult(woods))

for i in result:
    print(i)