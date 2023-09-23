# 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그 다음 사람에게만 던질 수 있다.
# 친구들의 번호가 들어있는 정수 배열 numbers
# 정수 k가 주어질 때
# k 번째로 공을 던지는 사람의 번호는 무엇인지 return

def solution(numbers, k):
    answer = ((k * 2) - 1) % len(numbers)
    if answer == 0:
        answer = numbers[-1]
    return answer


def solution(numbers, k):
    return numbers[((k * 2) - 1) % len(numbers)]