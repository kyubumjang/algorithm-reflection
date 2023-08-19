INF = 999999999 # 무한의 비용 선언

# 0, 1 사이에 7의 비용을 가진 간선, 0과 2 사이에 5 비용을 가진 간선
#   0
# 7/ \5
# 1   2

# 테이블로 표현하면
#    0  1   2
# 0  0  7   5
# 1  7  0  무한
# 2  5 무한  0

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
