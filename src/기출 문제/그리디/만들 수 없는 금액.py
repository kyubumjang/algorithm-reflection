# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성
# N = 5, 각 동전이 각각 3, 2, 1, 1, 9 동전이라고 가정할 때 만들 수 없는 양의 정수 금액 중 최솟값은 8원
# N = 3 3, 5, 7일 경우 만들수 없는 양의 정수 금액 중 최솟 값은 1원

n = int(input())
coin_type = list(map(int, input().split()))
coin_type.sort()

target = 1

for x in coin_type:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

print(target)
