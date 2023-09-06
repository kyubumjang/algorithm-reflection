# N가지 종류의 화폐, 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
# 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3월을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.

# 1 <= N <= 100
# 1 <= m <= 10000

n, m = map(int, input().split())

coin_types = []

for i in range(n):
    coin_types.append(int(input()))

#한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행 바텀업
d[0] = 0
for i in range(n):
    for j in range(coin_types[i], m + 1):
        if d[j - coin_types[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - coin_types[i]] + 1)

# 계삳된 결과 출력
if d[m] == 10001: #최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])