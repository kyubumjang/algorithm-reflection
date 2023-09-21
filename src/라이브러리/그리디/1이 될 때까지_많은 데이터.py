# N이 100억 이상의 큰 수가 되는 경우를 가정했을 때 빠르게 동작하려면,
# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드를 작성할 수 있다.

n, k = map(int, input().split())
result = 0

while True:
    # (N==K 로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    # N이 K보다ㅏ 작을 때 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)