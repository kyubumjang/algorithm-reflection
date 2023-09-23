# 숫자 Z가 공백으로 구분되어 담긴 문자열
# 문자열에 있는 숫자를 차례대로 더하기
# Z가 나오면 바로 전에 더했던 숫자를 뺀다

def solution(s):
    answer = 0
    s_list = []
    for i in range(len(s)):
        s_list = s.split(' ')

    print(s_list)
    for i in range(len(s_list)):
        if s_list[i] == 'Z':
            answer -= int(s_list[i - 1])
        if s_list[i] != 'Z':
            answer += int(s_list[i])
    return answer