# 여행에 필요하다고 생각하는 N개의 물건
# 각 물건은 무게 W와 가치 V를 가진다.
# 해당 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있다.
# 최대 K만큼 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 최대한 배낭에 넣을 수 있는 물건들의 가치의 최대값 출력

# 물품의 수 n, 준서가 버틸 수 있는 무게 k
n, k = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(k + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[n][k])