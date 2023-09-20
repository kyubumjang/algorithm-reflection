# 모험가 N명
# 공포도 측정, 공포도가 높은 모험가는 쉽게 공포를 느껴 위기 대처 능력 떨어짐
# 모험가 그룹 안전하게 구성하기 위해 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정
# 최대 몇 개의 모험가 그룹을 만들 수 있는지가 궁금함
# N명의 모험가에 대한 정보가 주어졌을 때 여행을 떠날 수 있는 그룹 수의 최댓값

n = int(input())
fear_list = list(map(int, input().split()))
fear_list.sort()

group = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in range(len(fear_list)):
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)

