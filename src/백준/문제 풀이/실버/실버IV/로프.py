n = int(input())
ropes = []

for _ in range(n):
    m = int(input())
    ropes.append(m)

ropes.sort(reverse=True)
result = []

for j in range(n):
    result.append(ropes[j] * (j - 1))

print(max(result))

