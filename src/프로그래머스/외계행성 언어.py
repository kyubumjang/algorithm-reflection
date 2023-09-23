import itertools


# 외계행성 언어
# 알파벳이 담긴 배열 spell
# 외계어 사전 dic
# 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재하면 1, 존재하지 않으면 2 return

def solution(spell, dic):
    answer = 0

    nPr = itertools.permutations(spell, len(spell))
    word_list = list(nPr)

    for i in range(len(word_list)):
        test_word = ""
        test_word = test_word.join(word_list[i])
        if dic.count(test_word) > 0:
            answer = 1
            break
        else:
            answer = 2

    return answer