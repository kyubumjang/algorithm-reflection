from itertools import combinations


def solution(nums):
    answer = 0

    result = 0
    combi = combinations(nums, 3)

    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for i in combi:
        for j in i:
            result += j
        if isPrime(result) == True:
            answer += 1
        result = 0

    return answer
