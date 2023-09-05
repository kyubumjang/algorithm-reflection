# 피보나치 함수를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# 이렇게 구현하면 동일한 함수가 반복적으로 호출된다.
# 이미 한 번 계산했지만, 계속 호출할 때마다 계산하는 것이다. O(2^n)의 지수 시간이 소요된다.
# 이런 경우 다이나믹 프로그래밍을 사용할 수 있다.

# 다이나밍 프로그래밍의 사용 조건
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.