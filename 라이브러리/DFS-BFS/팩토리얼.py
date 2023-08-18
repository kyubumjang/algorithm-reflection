# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성
    return n * factorial_recursive(n-1)

# 출력
print('반복적으로 구현: ', factorial_iterative(5))
print('재귀적으로 구현: ', factorial_recursive(5))

# 재귀 함수의 코드가 더 간결한 형태
# 점화식에서 종료 조건을 찾을 수 있다. 재귀 함수 내에서 특정 조건일 때 더 이상 재귀적으로 함수를 호출하지 않고 종료하도록 if문을 이용하여 꼭 종료 조건을 구현해줘야 한다.