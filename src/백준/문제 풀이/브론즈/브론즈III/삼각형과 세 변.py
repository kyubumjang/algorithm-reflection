# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.
# Equilateral: 세 변의 길이가 모두 같은 경우
# Isosceles: 두 변의 길이만 같은 경우
# Scalene: 세 변의 길이가 모두 다른 경우
# Invalid: 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우
# 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건에 만족하지 못한다.
import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    max_line = max(a, b, c)
    if a == 0 and b == 0 and c == 0:
        break
    if max_line >= a+b+c - max_line:
        print('Invalid')
        continue
    if a == b == c:
        print('Equilateral')
    if a != b and a != c and b != c:
        print('Scalene')
    if a == b and a != c or a != b and b == c or a == c and b != c:
        print('Isosceles')

